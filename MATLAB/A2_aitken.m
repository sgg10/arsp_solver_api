%Este programa halla la solución a la ecuación f(x)=0 usando el método de
%Aitken

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

function [x,iter,err]=A2_aitken(f,x0,tol,Nmax)

%Inicialización
E=1000;
cont=1;
tbl = [];

%Ciclo
while E>tol && cont<Nmax
  x1=f(x0);
  x2=f(x1);
  p=x0-((x1-x0)^2)/(x2-(2*x1)+x0);
  E=abs(p-x0);

  tbl = [tbl; cont,x0,x1,x2,p,E];
  

  cont=cont+1; 
  x0=p;
end

T = array2table(tbl, 'VariableNames',{'i' 'x' 'x1' 'x2' 'p' 'E'});
disp(T);

%Entrega de resultados
x=p;
iter=cont;
err=E;
end