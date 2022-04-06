%Este programa halla la solución a la ecuación f(x)=0 usando el método de
%la secante

%Entradas: 
%f, función continua
%x0, aproximación inicial
%x1, aproximación inicial
%tol, tolerancia
%Nmax, número máximo de iteraciones

%Salidas
%x, solución
%iter, número de iteraciones
%err, error

%Creado por: Samir Posada
%última actualización: 16/07/2020

function [x,iter,err]=C6_secante(f,x0,x1,tol,Nmax)

%Inicialización
f0=f(x0);
f1=f(x1);
E=1000; 
cont=0;
tbl = [cont,x0,f0, NaN];
cont=1;
tbl = [tbl; cont,x1,f1, NaN];

%Ciclo
while E>tol && cont<Nmax
  xact=x1-f1*(x1-x0)/(f1-f0);
  fact=f(xact);
  E=abs(xact-x1);
  cont=cont+1; 
  x0=x1;
  f0=f1;
  x1=xact;
  f1=fact;
  tbl = [tbl; cont,x1,f1,E];
end

T = array2table(tbl, 'VariableNames',{'i' 'x' 'f(x)' 'E'});
disp(T);

%Entrega de resultados
x=xact;
iter=cont;
err=E;
end 