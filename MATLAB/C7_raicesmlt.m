%Este programa halla la solución a la ecuación f(x)=0 usando el método de
%raíces múltiples

%Entradas: 
%f, función continua
%f', función continua
%f'', función continua
%x0, aproximación inicial 
%tol, tolerancia
%Nmax, número máximo de iteraciones

%Salidas
%x, solución
%iter, número de iteraciones
%err, error

%Creado por: Samir Posada
%última actualización: 16/07/2020

function [x,iter,err]=C7_raicesmlt(f,df,d2f,x0,tol,Nmax)

%Inicialización
xant=x0;
fant=f(xant);
E=1000; 
cont=0;
tbl = [cont,xant,fant,df(xant),d2f(xant),E];

%Ciclo
while E>tol && cont<Nmax
  xact=xant-fant*df(xant)/((df(xant))^2-fant*d2f(xant));
  fact=f(xact);
  E=abs(xact-xant);
  cont=cont+1;
  xant=xact;
  fant=fact;
  tbl = [tbl;cont,xant,fant,df(xant),d2f(xant),E];
end


T = array2table(tbl, 'VariableNames',{'i' 'x' 'f(x)' 'df(x)' 'd2f(x)' 'E'});
disp(T);

%Entrega de resultados
x=xact;
iter=cont;
err=E;
end 