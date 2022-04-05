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

function [x,iter,err]=A1_steffensen(f,x0,tol,Nmax)

%Inicialización
f0=f(x0);
g0=(f(x0+f0)/f0)-1;
E=1000;
cont=1;
tbl = [cont,x0,f0,g0,E];

%Ciclo
while E>tol && cont<Nmax
  xact=x0-(f0/g0);
  fact=f(xact);
  E=abs(xact-x0);
  cont=cont+1; 
  x0=xact;
  f0=fact;
  g0=(f(x0+f0)/f0)-1;
  tbl = [tbl; cont,x0,f0,g0,E];
end

T = array2table(tbl, 'VariableNames',{'i' 'x' 'f(x)' 'g(x)' 'E'});
disp(T);

%Entrega de resultados
x=xact;
iter=cont;
err=E;
end