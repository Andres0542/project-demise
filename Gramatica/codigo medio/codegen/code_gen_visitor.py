from gen.DemiseVisitor import DemiseVisitor


class CodeGenVisitor(DemiseVisitor):

    def __init__(self):
        self.sprites = {}       # tipo -> path (wall, floor, sky)
        self.map_grid = None    # lista 2D del mapa
        self.map_rows = 0
        self.map_cols = 0
        self.music_path = None
        self.npcs = []          # lista de (nombre, path)
        self.npc_positions = {} # nombre -> (x, y)
        self.weapons = []       # lista de (nombre, path)
        self.ui_path = None

    def visitSpriteDeclaration(self, ctx):
        sprite_type = ctx.SPRITE_TYPE().getText()
        path = ctx.STRING_LITERAL().getText().strip("'\"")
        self.sprites[sprite_type] = path

    def visitMapDeclaration(self, ctx):
        grid = []
        for row_ctx in ctx.mapRow():
            row = [int(tok.getText()) for tok in row_ctx.INTEGER()]
            if row:
                grid.append(row)

        if not grid:
            raise Exception("El mapa esta vacio o no contiene numeros validos")

        self.map_rows = len(grid)
        self.map_cols = len(grid[0])
        for fila in grid:
            if len(fila) != self.map_cols:
                raise Exception("Todas las filas del mapa deben tener el mismo tamano")

        self.map_grid = grid

    def visitMusicDeclaration(self, ctx):
        self.music_path = ctx.STRING_LITERAL().getText().strip("'\"")

    def visitNpcDeclaration(self, ctx):
        npc = ctx.ID().getText()
        path = ctx.STRING_LITERAL().getText().strip("'\"")
        self.npcs.append((npc, path))

    def visitNpcPositioning(self, ctx):
        npc = ctx.ID().getText()
        x = int(ctx.INTEGER(0).getText())
        y = int(ctx.INTEGER(1).getText())
        self.npc_positions[npc] = (x, y)

    def visitWeaponDeclaration(self, ctx):
        weapon = ctx.ID().getText()
        path = ctx.STRING_LITERAL().getText().strip("'\"")
        self.weapons.append((weapon, path))

    def visitUiDeclaration(self, ctx):
        self.ui_path = ctx.STRING_LITERAL().getText().strip("'\"")

    def finalizar(self):
        pass

    def _gen_includes(self):
        lines = []
        lines.append("#include <stdlib.h>")
        lines.append("#include <stdio.h>")
        lines.append("#include <GL/glut.h>")
        lines.append("#include <math.h>")
        if self.music_path:
            lines.append("#include <SDL2/SDL.h>")
            lines.append("#include <SDL2/SDL_mixer.h>")
        if self.sprites.get("wall"):
            lines.append(f'#include "{self.sprites["wall"]}"')
        if self.sprites.get("floor"):
            lines.append(f'#include "{self.sprites["floor"]}"')
        if self.sprites.get("sky"):
            lines.append(f'#include "{self.sprites["sky"]}"')
        return "\n".join(lines)

    def _gen_map_data(self):
        lines = []
        valores = []
        for fila in self.map_grid:
            valores.extend(fila)

        map_str = ",".join(map(str, valores))
        total = self.map_rows * self.map_cols

        lines.append(f"#define mapX {self.map_cols}")
        lines.append(f"#define mapY {self.map_rows}")
        lines.append("#define mapS 64")
        lines.append("")
        lines.append(f"int mapW[]= {{ {map_str} }};")
        lines.append("")
        zeros = ",".join(["0"] * total)
        lines.append(f"int mapF[]= {{ {zeros} }};")
        lines.append("")
        lines.append(f"int mapC[]= {{ {zeros} }};")
        return "\n".join(lines)

    def _gen_engine(self):
        has_sky = "sky" in self.sprites
        has_textures = "wall" in self.sprites

        texture_arr = "Alt_Textures"
        sky_arr = "sky"

        code = r"""
float degToRad(float a){ return a*M_PI/180.0;}
float FixAng(float a){ if(a>359){ a-=360;} if(a<0){ a+=360;} return a;}

float px,py,pdx,pdy,pa;
float frame1,frame2,fps;
int gameState=0;
typedef struct{ int w,a,d,s; }ButtonKeys;
ButtonKeys Keys;
int depth[120];

void drawMap2D(){
 int x,y,xo,yo;
 for(y=0;y<mapY;y++){
  for(x=0;x<mapX;x++){
   if(mapW[y*mapX+x]>0){ glColor3f(1,1,1);} else{ glColor3f(0,0,0);}
   xo=x*mapS; yo=y*mapS;
   glBegin(GL_QUADS);
   glVertex2i(xo+1,yo+1);
   glVertex2i(xo+1,mapS+yo-1);
   glVertex2i(mapS+xo-1,mapS+yo-1);
   glVertex2i(mapS+xo-1,yo+1);
   glEnd();
  }
 }
}

"""
        if has_sky:
            code += f"""void drawSky(){{
 int x,y;
 for(y=0;y<40;y++){{
  for(x=0;x<120;x++){{
   int xo=(int)pa*2-x; if(xo<0) xo+=120; xo=xo%120;
   int pixel=(y*120+xo)*3;
   int red={sky_arr}[pixel];
   int g={sky_arr}[pixel+1];
   int b={sky_arr}[pixel+2];
   glPointSize(8); glColor3ub(red,g,b); glBegin(GL_POINTS); glVertex2i(x*8,y*8); glEnd();
  }}
 }}
}}

"""

        if has_textures:
            code += f"""void drawRays2D(){{
 int r,mx,my,mp,dof,side; float vx,vy,rx,ry,ra,xo,yo,disV,disH;
 ra=FixAng(pa+30);
 for(r=0;r<120;r++){{
  int vmt=0,hmt=0;
  dof=0; side=0; disV=100000;
  float Tan=tan(degToRad(ra));
  if(cos(degToRad(ra))> 0.001){{ rx=(((int)px>>6)<<6)+64;      ry=(px-rx)*Tan+py; xo= 64; yo=-xo*Tan;}}
  else if(cos(degToRad(ra))<-0.001){{ rx=(((int)px>>6)<<6)-0.0001; ry=(px-rx)*Tan+py; xo=-64; yo=-xo*Tan;}}
  else {{ rx=px; ry=py; dof=8;}}
  while(dof<8){{
   mx=(int)(rx)>>6; my=(int)(ry)>>6; mp=my*mapX+mx;
   if(mp>0 && mp<mapX*mapY && mapW[mp]>0){{ vmt=mapW[mp]-1; dof=8; disV=cos(degToRad(ra))*(rx-px)-sin(degToRad(ra))*(ry-py);}}
   else{{ rx+=xo; ry+=yo; dof+=1;}}
  }}
  vx=rx; vy=ry;
  dof=0; disH=100000;
  Tan=1.0/Tan;
  if(sin(degToRad(ra))> 0.001){{ ry=(((int)py>>6)<<6)-0.0001; rx=(py-ry)*Tan+px; yo=-64; xo=-yo*Tan;}}
  else if(sin(degToRad(ra))<-0.001){{ ry=(((int)py>>6)<<6)+64;      rx=(py-ry)*Tan+px; yo= 64; xo=-yo*Tan;}}
  else{{ rx=px; ry=py; dof=8;}}
  while(dof<8){{
   mx=(int)(rx)>>6; my=(int)(ry)>>6; mp=my*mapX+mx;
   if(mp>0 && mp<mapX*mapY && mapW[mp]>0){{ hmt=mapW[mp]-1; dof=8; disH=cos(degToRad(ra))*(rx-px)-sin(degToRad(ra))*(ry-py);}}
   else{{ rx+=xo; ry+=yo; dof+=1;}}
  }}
  float shade=1;
  if(disV<disH){{ hmt=vmt; shade=0.5; rx=vx; ry=vy; disH=disV;}}
  int ca=FixAng(pa-ra); disH=disH*cos(degToRad(ca));
  int lineH=(mapS*640)/(disH);
  float ty_step=32.0/(float)lineH;
  float ty_off=0;
  if(lineH>640){{ ty_off=(lineH-640)/2.0; lineH=640;}}
  int lineOff=320-(lineH>>1);
  depth[r]=disH;
  int y;
  float ty=ty_off*ty_step;
  float tx;
  if(shade==1){{ tx=(int)(rx/2.0)%32; if(ra>180){{ tx=31-tx;}} }}
  else        {{ tx=(int)(ry/2.0)%32; if(ra>90 && ra<270){{ tx=31-tx;}} }}
  for(y=0;y<lineH;y++){{
   int pixel=((int)ty*32+(int)tx)*3+(hmt*32*32*3);
   int red={texture_arr}[pixel]*shade;
   int g={texture_arr}[pixel+1]*shade;
   int b={texture_arr}[pixel+2]*shade;
   glPointSize(8); glColor3ub(red,g,b); glBegin(GL_POINTS); glVertex2i(r*8,y+lineOff); glEnd();
   ty+=ty_step;
  }}
  for(y=lineOff+lineH;y<640;y++){{
   float dy=y-(640/2.0), deg=degToRad(ra), raFix=cos(degToRad(FixAng(pa-ra)));
   tx=px/2+cos(deg)*158*2*32/dy/raFix;
   ty=py/2-sin(deg)*158*2*32/dy/raFix;
   int mp2=mapF[(int)(ty/32.0)*mapX+(int)(tx/32.0)]*32*32;
   int pixel=(((int)(ty)&31)*32+((int)(tx)&31))*3+mp2*3;
   int red={texture_arr}[pixel]*0.7;
   int g={texture_arr}[pixel+1]*0.7;
   int b={texture_arr}[pixel+2]*0.7;
   glPointSize(8); glColor3ub(red,g,b); glBegin(GL_POINTS); glVertex2i(r*8,y); glEnd();
   mp2=mapC[(int)(ty/32.0)*mapX+(int)(tx/32.0)]*32*32;
   pixel=(((int)(ty)&31)*32+((int)(tx)&31))*3+mp2*3;
   red={texture_arr}[pixel];
   g={texture_arr}[pixel+1];
   b={texture_arr}[pixel+2];
   if(mp2>0){{ glPointSize(8); glColor3ub(red,g,b); glBegin(GL_POINTS); glVertex2i(r*8,640-y); glEnd();}}
  }}
  ra=FixAng(ra-0.5);
 }}
}}

"""
        else:
            code += """void drawRays2D(){
 int r,mx,my,mp,dof; float rx,ry,ra,xo,yo,disV,disH;
 ra=FixAng(pa+30);
 for(r=0;r<120;r++){
  dof=0; disV=100000;
  float Tan=tan(degToRad(ra));
  if(cos(degToRad(ra))> 0.001){ rx=(((int)px>>6)<<6)+64; ry=(px-rx)*Tan+py; xo=64; yo=-xo*Tan;}
  else if(cos(degToRad(ra))<-0.001){ rx=(((int)px>>6)<<6)-0.0001; ry=(px-rx)*Tan+py; xo=-64; yo=-xo*Tan;}
  else { rx=px; ry=py; dof=8;}
  while(dof<8){
   mx=(int)(rx)>>6; my=(int)(ry)>>6; mp=my*mapX+mx;
   if(mp>0 && mp<mapX*mapY && mapW[mp]>0){ dof=8; disV=cos(degToRad(ra))*(rx-px)-sin(degToRad(ra))*(ry-py);}
   else{ rx+=xo; ry+=yo; dof+=1;}
  }
  float vx=rx,vy=ry;
  dof=0; disH=100000;
  Tan=1.0/Tan;
  if(sin(degToRad(ra))> 0.001){ ry=(((int)py>>6)<<6)-0.0001; rx=(py-ry)*Tan+px; yo=-64; xo=-yo*Tan;}
  else if(sin(degToRad(ra))<-0.001){ ry=(((int)py>>6)<<6)+64; rx=(py-ry)*Tan+px; yo=64; xo=-yo*Tan;}
  else{ rx=px; ry=py; dof=8;}
  while(dof<8){
   mx=(int)(rx)>>6; my=(int)(ry)>>6; mp=my*mapX+mx;
   if(mp>0 && mp<mapX*mapY && mapW[mp]>0){ dof=8; disH=cos(degToRad(ra))*(rx-px)-sin(degToRad(ra))*(ry-py);}
   else{ rx+=xo; ry+=yo; dof+=1;}
  }
  glColor3f(0,0.8,0);
  if(disV<disH){ disH=disV; rx=vx; ry=vy; glColor3f(0,0.6,0);}
  int ca=FixAng(pa-ra); disH=disH*cos(degToRad(ca));
  int lineH=(mapS*640)/(disH);
  if(lineH>640){ lineH=640;}
  int lineOff=320-(lineH>>1);
  depth[r]=disH;
  glLineWidth(8); glBegin(GL_LINES); glVertex2i(r*8,lineOff); glVertex2i(r*8,lineOff+lineH); glEnd();
  ra=FixAng(ra-0.5);
 }
}

"""

        code += """void Movement(){
 if(Keys.a==1){ pa+=0.2*fps; pa=FixAng(pa); pdx=cos(degToRad(pa)); pdy=-sin(degToRad(pa));}
 if(Keys.d==1){ pa-=0.2*fps; pa=FixAng(pa); pdx=cos(degToRad(pa)); pdy=-sin(degToRad(pa));}
 int xo=0; if(pdx<0){ xo=-20;} else{ xo=20;}
 int yo=0; if(pdy<0){ yo=-20;} else{ yo=20;}
 int ipx=px/64.0, ipx_add_xo=(px+xo)/64.0, ipx_sub_xo=(px-xo)/64.0;
 int ipy=py/64.0, ipy_add_yo=(py+yo)/64.0, ipy_sub_yo=(py-yo)/64.0;
 if(Keys.w==1){
  if(mapW[ipy*mapX+ipx_add_xo]==0){ px+=pdx*0.2*fps;}
  if(mapW[ipy_add_yo*mapX+ipx]==0){ py+=pdy*0.2*fps;}
 }
 if(Keys.s==1){
  if(mapW[ipy*mapX+ipx_sub_xo]==0){ px-=pdx*0.2*fps;}
  if(mapW[ipy_sub_yo*mapX+ipx]==0){ py-=pdy*0.2*fps;}
 }
}

void init(){
 glClearColor(0.3,0.3,0.3,0);
 px=150; py=400; pa=90;
 pdx=cos(degToRad(pa)); pdy=-sin(degToRad(pa));
}

void display(){
 frame2=glutGet(GLUT_ELAPSED_TIME); fps=(frame2-frame1); frame1=glutGet(GLUT_ELAPSED_TIME);
 Movement();
 glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT);
"""
        if has_sky:
            code += " drawSky();\n"
        code += """ drawRays2D();
 glutPostRedisplay();
 glutSwapBuffers();
}

void ButtonDown(unsigned char key,int x,int y){
 if(key=='a'){ Keys.a=1;}
 if(key=='d'){ Keys.d=1;}
 if(key=='w'){ Keys.w=1;}
 if(key=='s'){ Keys.s=1;}
 if(key=='e'){
  int xo=0; if(pdx<0){ xo=-25;} else{ xo=25;}
  int yo=0; if(pdy<0){ yo=-25;} else{ yo=25;}
  int ipx=px/64.0, ipx_add_xo=(px+xo)/64.0;
  int ipy=py/64.0, ipy_add_yo=(py+yo)/64.0;
  if(mapW[ipy_add_yo*mapX+ipx_add_xo]==4){ mapW[ipy_add_yo*mapX+ipx_add_xo]=0;}
 }
 glutPostRedisplay();
}

void ButtonUp(unsigned char key,int x,int y){
 if(key=='a'){ Keys.a=0;}
 if(key=='d'){ Keys.d=0;}
 if(key=='w'){ Keys.w=0;}
 if(key=='s'){ Keys.s=0;}
 glutPostRedisplay();
}

void resize(int w,int h){ glutReshapeWindow(960,640);}
"""
        return code

    def _gen_main(self):
        lines = []
        lines.append("int main(int argc, char* argv[]){")
        lines.append(" glutInit(&argc, argv);")
        lines.append(" glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB);")
        lines.append(" glutInitWindowSize(960,640);")
        lines.append(" glutInitWindowPosition(glutGet(GLUT_SCREEN_WIDTH)/2-480,glutGet(GLUT_SCREEN_HEIGHT)/2-320);")
        lines.append(' glutCreateWindow("Demise Engine");')

        if self.music_path:
            lines.append(" if(SDL_Init(SDL_INIT_AUDIO)<0){ printf(\"Error SDL Audio: %s\\n\",SDL_GetError());}")
            lines.append(" if(Mix_OpenAudio(44100,MIX_DEFAULT_FORMAT,2,2048)<0){ printf(\"Error Mix: %s\\n\",Mix_GetError());}")
            lines.append(f' Mix_Music *bgm=Mix_LoadMUS("{self.music_path}");')
            lines.append(" if(!bgm){ printf(\"No se pudo cargar musica: %s\\n\",Mix_GetError());}")
            lines.append(" else{ Mix_PlayMusic(bgm,-1);}")

        lines.append(" gluOrtho2D(0,960,640,0);")
        lines.append(" init();")
        lines.append(" glutDisplayFunc(display);")
        lines.append(" glutReshapeFunc(resize);")
        lines.append(" glutKeyboardFunc(ButtonDown);")
        lines.append(" glutKeyboardUpFunc(ButtonUp);")
        lines.append(" glutMainLoop();")

        if self.music_path:
            lines.append(" Mix_FreeMusic(bgm);")
            lines.append(" Mix_CloseAudio();")
            lines.append(" SDL_Quit();")

        lines.append(" return 0;")
        lines.append("}")
        return "\n".join(lines)

    def emitir(self, archivo="salida.c"):
        partes = []
        partes.append(self._gen_includes())
        partes.append("")
        partes.append(self._gen_map_data())
        partes.append("")
        partes.append(self._gen_engine())
        partes.append(self._gen_main())
        partes.append("")

        codigo_final = "\n".join(partes)

        with open(archivo, "w", encoding="utf-8") as f:
            f.write(codigo_final)

        return codigo_final