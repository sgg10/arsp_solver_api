%Este programa halla la solución a la ecuación f(x)=0 usando el método de
%Newton

%Entradas: 
%f, función continua
%f', función continua
%x0, aproximación inicial 
%tol, tolerancia
%Nmax, número máximo de iteraciones

%Salidas
%x, solución
%iter, número de iteraciones
%err, error

%Creado por: Samir Posada
%última actualización: 16/07/2020

function [x,iter,err]=C5_newton(f,df,x0,tol,Nmax)

%Inicialización
xant=x0;
fant=f(xant);
dfant=df(xant);
E=1000; 
cont=0;

tbl = [cont,xant,fant,dfant,E];

%Ciclo
while E>tol && cont<Nmax
  xact=xant-fant/(df(xant));
  fact=f(xact);
  dfact=df(xact);
  E=abs(xact-xant);
  cont=cont+1;
  xant=xact;
  fant=fact;
  dfant=dfact;
  tbl = [tbl; cont,xant,fant,dfant,E];
end

T = array2table(tbl, 'VariableNames',{'i' 'x' 'f(x)' 'df(x)' 'E'});
disp(T);

%Entrega de resultados
x=xact;
iter=cont;
err=E;
end 