%Este programa halla la solución a la ecuación f(x)=0 en el intervalo [a,b]
%usando el método de la bisección. 

%Entradas: 
%f, función continua
%a, extremo derecho del intervalo inicial
%b, extremo final del intervalo final
%tol, tolerancia
%Nmax, número máximo de iteraciones

%Salidas
%x, solución
%iter, número de iteraciones
%err, error

%Creado por: Samir Posada
%última actualización: 16/07/2020

function [x,iter,err, T]=C2_biseccion(f,a,b,tol,Nmax)

%Inicialización
fa=f(a);
fb=f(b);
pm=(a+b)/2;
fpm=f(pm);
E=10000000000000;
cont=1;

tbl = [];

%Ciclo
while E>tol && cont<Nmax
  tbl = [tbl;cont,a,fa,b,fb,E];
  if fa*fpm<0
     b=pm; 
  else
     a=pm;    
  end
  p0=pm;
  pm=(a+b)/2;
  fpm=f(pm);
  E=abs(pm-p0);
  cont=cont+1;
  fa=f(a);
  fb=f(b);
end

%Crear tabla a mostrar
T = array2table(tbl, 'VariableNames',{'i' 'a' 'f(a)' 'b' 'f(b)' 'E'});
disp(T);

%Entrega de resultados
x=pm;
iter=cont;
err=E;
end