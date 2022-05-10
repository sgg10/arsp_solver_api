%Este programa halla la solución a la ecuación f(x)=0 usando el método de
%Steffensen

%Entradas: 
%f, función continua
%x0, aproximación inicial
%tol, tolerancia
%Nmax, número máximo de iteraciones

%Salidas
%x, solución
%iter, número de iteraciones
%err, error

%Creado por: Pascual Gómez
%última actualización: 04/04/2022

function [x,iter,err]=A7_parcial2(f,df,d2f,x0,tol,Nmax)

%Inicialización
f0=f(x0);
df0=df(x0);
d2f0 = d2f(x0);

g0= f0 * d2f0 - (df0^2) - (f0^3);

E=1000;
cont=1;
tbl = [cont,x0,f0,E];

%Ciclo
while E>tol && cont<Nmax
  xact = x0 - ( ( f0*df0-(f0^3) ) / g0 );

  fact=f(xact);
  dfact=df(xact);
  d2fact=d2f(xact);

  E=abs(xact-x0);
  cont=cont+1;

  x0=xact;
  f0=fact;
  df0=dfact;
  d2f0=d2fact;

  g0 = f0 * d2f0 - (df0^2) - (f0^3);
  
  tbl = [tbl; cont,x0,f0,E];
end

T = array2table(tbl, 'VariableNames',{'i' 'x' 'f(x)' 'E'});
disp(T);

%Entrega de resultados
x=xact;
iter=cont;
err=E;
end