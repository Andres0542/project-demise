//------------------------YouTube-3DSage----------------------------------------
//Full video: https://youtu.be/PC1RaETIx3Y
//WADS to move player.

#include <stdlib.h>
#include <GL/glut.h>
#include <math.h>
#include <SDL2/SDL.h>
#include <SDL2/SDL_mixer.h>
#include "Textures/Alt_Textures.ppm"
#include "Textures/sky.ppm"
#include "Textures/title.ppm"
#include "Textures/won.ppm"
#include "Textures/lost.ppm"
float degToRad(float a) { return a*M_PI/180.0;}
float FixAng(float a){ if(a>359){ a-=360;} if(a<0){ a+=360;} return a;}
float distance(float ax, float ay, float bx, float by, float ang){ return cos(degToRad(ang))*(bx-ax)-sin(degToRad(ang))*(by-ay);}
float px,py,pdx,pdy,pa;
float frame1,frame2,fps;

typedef struct
{
 int w,a,d,s;                     //button state on off
}ButtonKeys; ButtonKeys Keys;

//-----------------------------MAP----------------------------------------------
#define mapX  8      //map width
#define mapY  8      //map height
#define mapS 64      //map cube size

                     //Edit these 3 arrays with values 0-4 to create your own level! 
int mapW[]=          //walls
{
 1,1,1,1,1,3,1,1,
 1,0,0,1,0,0,0,1,
 1,0,0,4,0,2,0,1,
 1,1,4,1,0,0,0,1,
 2,0,0,0,0,0,0,1,
 2,0,0,0,0,1,0,1,
 2,0,0,0,0,0,0,1,
 1,1,3,1,3,1,3,1,	
};

int mapF[]=          //floors
{
 0,0,0,0,0,0,0,0,
 0,0,0,0,1,1,0,0,
 0,0,0,0,2,0,0,0,
 0,0,0,0,0,0,0,0,
 0,0,2,0,0,0,0,0,
 0,0,0,0,0,0,0,0,
 0,1,1,1,1,0,0,0,
 0,0,0,0,0,0,0,0,	
};

int mapC[]=          //ceiling
{
 0,0,0,0,0,0,0,0,
 0,0,0,0,0,0,0,0,
 0,0,0,0,0,0,0,0,
 0,0,0,0,0,0,1,0,
 0,1,3,1,0,0,0,0,
 0,0,0,0,0,0,0,0,
 0,0,0,0,0,0,0,0,
 0,0,0,0,0,0,0,0,	
};

void drawMap2D()
{
 int x,y,xo,yo;
 for(y=0;y<mapY;y++)
 {
  for(x=0;x<mapX;x++)
  {
   if(mapW[y*mapX+x]>0){ glColor3f(1,1,1);} else{ glColor3f(0,0,0);}
   xo=x*mapS; yo=y*mapS;
   glBegin(GL_QUADS); 
   glVertex2i( 0   +xo+1, 0   +yo+1); 
   glVertex2i( 0   +xo+1, mapS+yo-1); 
   glVertex2i( mapS+xo-1, mapS+yo-1);  
   glVertex2i( mapS+xo-1, 0   +yo+1); 
   glEnd();
  } 
 } 
}//-----------------------------------------------------------------------------


//------------------------PLAYER------------------------------------------------
void drawPlayer2D()
{
 glColor3f(1,1,0);   glPointSize(8);    glLineWidth(4);
 glBegin(GL_POINTS); glVertex2i(px,py); glEnd();
 glBegin(GL_LINES);  glVertex2i(px,py); glVertex2i(px+pdx*20,py+pdy*20); glEnd();
}//-----------------------------------------------------------------------------

void drawSky(){
     int x,y;
     for(y=0;y<40;y++){
           for(x=0;x<120;x++){
                int xo = (int)pa*2-x;if(xo<0)xo+=120; xo = xo % 120; 
                int pixel = (y*120+xo)*3;
                int red = sky[pixel];
                int g = sky[pixel+1];
                int b = sky[pixel+2];
                glPointSize(8); glColor3ub(red,g,b); glBegin(GL_POINTS); glVertex2i(x*8,y*8); glEnd();
           }
      }
}

//---------------------------Draw Rays and Walls--------------------------------
void drawRays2D()
{
 //glColor3f(0,1,1); glBegin(GL_QUADS); glVertex2i(526,  0); glVertex2i(1006,  0); glVertex2i(1006,160); glVertex2i(526,160); glEnd();	
 //glColor3f(0,0,1); glBegin(GL_QUADS); glVertex2i(526,160); glVertex2i(1006,160); glVertex2i(1006,320); glVertex2i(526,320); glEnd();	 	
	
 int r,mx,my,mp,dof,side; float vx,vy,rx,ry,ra,xo,yo,disV,disH; 
 
 ra=FixAng(pa+30);                                                              //ray set back 30 degrees
 
 for(r=0;r<120;r++)
 {
  int vmt=0,hmt=0;                                                              //vertical and horizontal map texture number 
  //---Vertical--- 
  dof=0; side=0; disV=100000;
  float Tan=tan(degToRad(ra));
       if(cos(degToRad(ra))> 0.001){ rx=(((int)px>>6)<<6)+64;      ry=(px-rx)*Tan+py; xo= 64; yo=-xo*Tan;}//looking left
  else if(cos(degToRad(ra))<-0.001){ rx=(((int)px>>6)<<6) -0.0001; ry=(px-rx)*Tan+py; xo=-64; yo=-xo*Tan;}//looking right
  else { rx=px; ry=py; dof=8;}                                                  //looking up or down. no hit  

  while(dof<8) 
  { 
   mx=(int)(rx)>>6; my=(int)(ry)>>6; mp=my*mapX+mx;                     
   if(mp>0 && mp<mapX*mapY && mapW[mp]>0){ vmt=mapW[mp]-1; dof=8; disV=cos(degToRad(ra))*(rx-px)-sin(degToRad(ra))*(ry-py);}//hit         
   else{ rx+=xo; ry+=yo; dof+=1;}                                               //check next horizontal
  } 
  vx=rx; vy=ry;

  //---Horizontal---
  dof=0; disH=100000;
  Tan=1.0/Tan; 
       if(sin(degToRad(ra))> 0.001){ ry=(((int)py>>6)<<6) -0.0001; rx=(py-ry)*Tan+px; yo=-64; xo=-yo*Tan;}//looking up 
  else if(sin(degToRad(ra))<-0.001){ ry=(((int)py>>6)<<6)+64;      rx=(py-ry)*Tan+px; yo= 64; xo=-yo*Tan;}//looking down
  else{ rx=px; ry=py; dof=8;}                                                   //looking straight left or right
 
  while(dof<8) 
  { 
   mx=(int)(rx)>>6; my=(int)(ry)>>6; mp=my*mapX+mx;                          
   if(mp>0 && mp<mapX*mapY && mapW[mp]>0){ hmt=mapW[mp]-1; dof=8; disH=cos(degToRad(ra))*(rx-px)-sin(degToRad(ra))*(ry-py);}//hit         
   else{ rx+=xo; ry+=yo; dof+=1;}                                               //check next horizontal
  } 
  
  float shade=1;
  glColor3f(0,0.8,0);
  if(disV<disH){ hmt=vmt; shade=0.5; rx=vx; ry=vy; disH=disV; glColor3f(0,0.6,0);}//horizontal hit first
  //glLineWidth(2); glBegin(GL_LINES); glVertex2i(px,py); glVertex2i(rx,ry); glEnd();//draw 2D ray
    
  int ca=FixAng(pa-ra); disH=disH*cos(degToRad(ca));                            //fix fisheye 
  int lineH = (mapS*640)/(disH); 
  float ty_step=32.0/(float)lineH; 
  float ty_off=0; 
  if(lineH>640){ ty_off=(lineH-640)/2.0; lineH=640;}                            //line height and limit
  int lineOff = 320 - (lineH>>1);                                               //line offset

  //---draw walls---
  int y;
  float ty=ty_off*ty_step;//+hmt*32;
  float tx;
  if(shade==1){ tx=(int)(rx/2.0)%32; if(ra>180){ tx=31-tx;}}  
  else        { tx=(int)(ry/2.0)%32; if(ra>90 && ra<270){ tx=31-tx;}}
  for(y=0;y<lineH;y++){
     int pixel = ((int)ty*32+(int)tx)*3/*Cambiar las texturas*/+(hmt*32*32*3);
     int red = Alt_Textures[pixel]*shade;
     int g = Alt_Textures[pixel+1]*shade;
     int b = Alt_Textures[pixel+2]*shade;
     glPointSize(8); glColor3ub(red,g,b); glBegin(GL_POINTS); glVertex2i(r*8,y+lineOff); glEnd();
     ty+=ty_step;
}
   //float c=All_Textures[(int)(ty)*32 + (int)(tx)]*shade;
   //if(hmt==0){ glColor3f(c    , c/2.0, c/2.0);} //checkerboard red
   //if(hmt==1){ glColor3f(c    , c    , c/2.0);} //Brick yellow
   //if(hmt==2){ glColor3f(c/2.0, c/2.0, c    );} //window blue
   //if(hmt==3){ glColor3f(c/2.0, c    , c/2.0);} //door green
   //glPointSize(8);glBegin(GL_POINTS);glVertex2i(r*8+530,y+lineOff);glEnd();//draw vertical wall  
   //ty+=ty_step;
 
  //---draw floors---
 for(y=lineOff+lineH;y<640;y++)
 {
  float dy=y-(640/2.0), deg=degToRad(ra), raFix=cos(degToRad(FixAng(pa-ra)));
  tx=px/2 + cos(deg)*158*32/dy/raFix;
  ty=py/2 - sin(deg)*158*32/dy/raFix;
  int mp=mapF[(int)(ty/32.0)*mapX+(int)(tx/32.0)]*32*32;
  int pixel = (((int)(ty)&31)*32+((int)(tx)&31))*3+mp*3;
  int red = Alt_Textures[pixel];
  int g = Alt_Textures[pixel+1];
  int b = Alt_Textures[pixel+2];
  glPointSize(8); glColor3ub(red,g,b); glBegin(GL_POINTS); glVertex2i(r*8,y); glEnd();
  //ty+=ty_step;
  //float c=All_Textures[((int)(ty)&31)*32 + ((int)(tx)&31)+mp]*0.7;
  //glColor3f(c/1.3,c/1.3,c);glPointSize(8);glBegin(GL_POINTS);glVertex2i(r*8+530,y);glEnd();

 //---draw ceiling---
  mp=mapC[(int)(ty/32.0)*mapX+(int)(tx/32.0)]*32*32;
  //c=All_Textures[((int)(ty)&31)*32 + ((int)(tx)&31)+mp]*0.7;
  //glColor3f(c/2.0,c/1.2,c/2.0);glPointSize(8);glBegin(GL_POINTS);glVertex2i(r*8+530,320-y);glEnd();

  pixel = (((int)(ty)&31)*32+((int)(tx)&31))*3+mp*3;
  red = Alt_Textures[pixel];
  g = Alt_Textures[pixel+1];
  b = Alt_Textures[pixel+2];
  if(mp>0){glPointSize(8); glColor3ub(red,g,b); glBegin(GL_POINTS); glVertex2i(r*8,640-y); glEnd();}
  //ty+=ty_step;
 }
 
 ra=FixAng(ra-0.5);                                                               //go to next ray, 60 total
 }
}//-----------------------------------------------------------------------------


void init()
{
 glClearColor(0.3,0.3,0.3,0);
 //gluOrtho2D(0,960,640,0);
 px=150; py=400; pa=90;
 pdx=cos(degToRad(pa)); pdy=-sin(degToRad(pa));                                 //init player
}

void screen(int v){
     int x,y; int *T;
     if (v==0){ T=title;}
     if (v==1){ T=won;}
     if (v==2){ T=lost;}
     for(y=0;y<80;y++){
           for(x=0;x<120;x++){
                int pixel = (y*120+x)*3;
                int red = T[pixel];
                int g = T[pixel+1];
                int b = T[pixel+2];
                glPointSize(8); glColor3ub(red,g,b); glBegin(GL_POINTS); glVertex2i(x*8,y*8); glEnd();
           }
      }
}

int gameState=0, timer=0;
void display()
{  
 //frames per second
 frame2=glutGet(GLUT_ELAPSED_TIME); fps=(frame2-frame1); frame1=glutGet(GLUT_ELAPSED_TIME); 

 if (gameState==0){ init(); timer=0; gameState=1;}
 if (gameState==1){ screen(0);timer+=1*fps; if(timer>3000){ timer=0; gameState=2;}}
 if (gameState==2){
     //buttons
     if(Keys.a==1){ pa+=0.2*fps; pa=FixAng(pa); pdx=cos(degToRad(pa)); pdy=-sin(degToRad(pa));} 	
     if(Keys.d==1){ pa-=0.2*fps; pa=FixAng(pa); pdx=cos(degToRad(pa)); pdy=-sin(degToRad(pa));} 
     int xo=0; if(pdx<0){ xo=-20;} else{ xo=20;}                                    //x offset to check map
     int yo=0; if(pdy<0){ yo=-20;} else{ yo=20;}                                    //y offset to check map
     int ipx=px/64.0, ipx_add_xo=(px+xo)/64.0, ipx_sub_xo=(px-xo)/64.0;             //x position and offset
     int ipy=py/64.0, ipy_add_yo=(py+yo)/64.0, ipy_sub_yo=(py-yo)/64.0;             //y position and offset
     if(Keys.w==1){
          if(mapW[ipy*mapX        + ipx_add_xo]==0){ px+=pdx*0.2*fps;}
          if(mapW[ipy_add_yo*mapX + ipx       ]==0){ py+=pdy*0.2*fps;}
     }  //move forward                                                                
     if(Keys.s==1){
     if(mapW[ipy*mapX        + ipx_sub_xo]==0){ px-=pdx*0.2*fps;}
     if(mapW[ipy_sub_yo*mapX + ipx       ]==0){ py-=pdy*0.2*fps;}
     } //move backward 
     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
     drawSky(); 
     //drawMap2D();
     // //drawPlayer2D();
     drawRays2D();
 }
 glutPostRedisplay();
 glutSwapBuffers();  
}

void ButtonDown(unsigned char key,int x,int y)                                  //keyboard button pressed down
{
 if(key=='a'){ Keys.a=1;} 	
 if(key=='d'){ Keys.d=1;} 
 if(key=='w'){ Keys.w=1;}
 if(key=='s'){ Keys.s=1;}
 if(key=='e')             //open doors
 { 
  int xo=0; if(pdx<0){ xo=-25;} else{ xo=25;}
  int yo=0; if(pdy<0){ yo=-25;} else{ yo=25;} 
  int ipx=px/64.0, ipx_add_xo=(px+xo)/64.0;
  int ipy=py/64.0, ipy_add_yo=(py+yo)/64.0;
  if(mapW[ipy_add_yo*mapX+ipx_add_xo]==4){ mapW[ipy_add_yo*mapX+ipx_add_xo]=0;}
 }

 glutPostRedisplay();
}

void ButtonUp(unsigned char key,int x,int y)                                    //keyboard button pressed up
{
 if(key=='a'){ Keys.a=0;} 	
 if(key=='d'){ Keys.d=0;} 
 if(key=='w'){ Keys.w=0;}
 if(key=='s'){ Keys.s=0;}
 glutPostRedisplay();
}

void resize(int w,int h)                                                        //screen window rescaled, snap back
{
 glutReshapeWindow(960,640);
}

/*int main(int argc, char* argv[])
{ 
 glutInit(&argc, argv);
 glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
 glutInitWindowSize(1024,510);
 glutInitWindowPosition(200,200);
 glutCreateWindow("YouTube-3DSage");
 init();
 glutDisplayFunc(display);
 glutReshapeFunc(resize);
 glutKeyboardFunc(ButtonDown);
 glutKeyboardUpFunc(ButtonUp);
 glutMainLoop();
}*/

int main(int argc, char* argv[])
{ 
 glutInit(&argc, argv);
 glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
 glutInitWindowSize(960,640);
 glutInitWindowPosition(glutGet(GLUT_SCREEN_WIDTH)/2-960/2, glutGet(GLUT_SCREEN_HEIGHT)/2-640/2);
 glutCreateWindow("YouTube-3DSage");
 
 // --- INICIALIZAR AUDIO CON SDL2 ---
 if (SDL_Init(SDL_INIT_AUDIO) < 0) {
     printf("Error inicializando SDL Audio: %s\n", SDL_GetError());
 }
 
 // Abrir canales de audio (44100Hz, formato por defecto, 2 canales estéreo, buffer de 2048)
 if (Mix_OpenAudio(44100, MIX_DEFAULT_FORMAT, 2, 2048) < 0) {
     printf("Error en Mix_OpenAudio: %s\n", Mix_GetError());
 }

 // Cargar tu archivo de música (Soporta .mp3, .wav, .ogg)
 Mix_Music *bgm = Mix_LoadMUS("soundtrack.mp3");
 if (!bgm) {
     printf("No se pudo cargar la música: %s\n", Mix_GetError());
 } else {
     // Reproducir en bucle infinito (-1 significa loop infinito)
     Mix_PlayMusic(bgm, -1); 
 }
 // ----------------------------------
 gluOrtho2D(0,960,640,0);
 init();
 glutDisplayFunc(display);
 glutReshapeFunc(resize);
 glutKeyboardFunc(ButtonDown);
 glutKeyboardUpFunc(ButtonUp);
 
 glutMainLoop();

 // Limpieza al salir (opcional, GLUT rara vez llega aquí debido a su bucle infinito)
 Mix_FreeMusic(bgm);
 Mix_CloseAudio();
 SDL_Quit();
 return 0;
}
