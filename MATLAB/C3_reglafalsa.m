%Este programa halla la solución a la ecuación f(x)=0 en el intervalo [a,b]
%usando el método de la regla falsa

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

function [x,iter,err]=C3_reglafalsa(f,a,b,tol,Nmax)

%Inicialización
fa=f(a);
fb=f(b);
pm=(fb*a-fa*b)/(fb-fa);
fpm=f(pm);
E=1000; 
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
  pm=(f(b)*a-f(a)*b)/(f(b)-f(a));
  fpm=f(pm);
  E=abs(pm-p0);
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