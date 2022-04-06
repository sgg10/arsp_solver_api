%Este programa halla la solución a la ecuación f(x)=0 resolviendo el problema
%análogo x=g(x) usando el método de punto fijo. 

%Entradas: 
%f, función continua
%g, función continua
%x0, aproximación inicial 
%tol, tolerancia
%Nmax, número máximo de iteraciones

%Salidas
%x, solución
%iter, número de iteraciones
%err, error

%Creado por: Samir Posada
%última actualización: 16/07/2020

function [x,iter,err]=C4_puntofijo(g,x0,tol,Nmax)

%Inicialización
xant=x0;
E=1000; 
cont=0;

tbl = [cont,xant,g(xant),NaN];


%Ciclo
while E>tol && cont<Nmax
  xact=g(xant);
  E=abs(xact-xant);
  cont=cont+1;
  xant=xact;
  tbl = [tbl;cont,xant,xact,E];
end

T = array2table(tbl, 'VariableNames',{'i' 'x' 'f(x)' 'E'});
disp(T);

%Entrega de resultados
x=xact;
iter=cont;
err=E;
end