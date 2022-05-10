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

function [x,iter,err]=C2_biseccion(f,a,b,tol,Nmax)

%Inicialización
fa=f(a);
fb=f(b);
pm=(a+b)/2;
fpm=f(pm);
E=10000;
cont=1;

tbl = [cont,a,fa,b,fb,NaN];

%Ciclo
while E>tol && cont<Nmax
  if fa*fpm<0
     b=pm; 
  else
     a=pm;    
  end
  p0=pm;
  pm=(a+b)/2;
  fpm=f(pm);
  format shortE
  E=abs(pm-p0);
  format short
  cont=cont+1;
  fa=f(a);
  fb=f(b);
  tbl = [tbl;cont,a,fa,b,fb,E];
end

%Crear tabla a mostrar
T = array2table(tbl, 'VariableNames',{'i' 'a' 'f(a)' 'b' 'f(b)' 'E'});
disp(T);

%Entrega de resultados
x=pm;
iter=cont;
err=E;
end