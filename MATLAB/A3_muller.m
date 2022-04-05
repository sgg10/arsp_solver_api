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

function [x,iter,err]=A3_muller(f,x0,x1,x2,tol,Nmax)

%Inicialización
E=1000;
cont=1;
tbl = [];
h1 = x1 - x0;
h2 = x2 - x1;
delta1 = (f(x1) - f(x0))/h1;
delta2 = (f(x2) - f(x1))/h2;
d = (delta2 - delta1)/(h2 + h1);


while E>tol && cont<Nmax
      b = delta2 + h2*d;
      D = (b^2 - 4*f(x2)*d)^(1/2);

      if abs(b-D) < abs(b+D)
          E = b + D;
      else
          E = b - D;
      end
      h = -2*f(x2)/E;
      p = x2 + h;
      E = abs(h);

      tbl = [tbl; cont,x0,x1,x2,p,E];

      x0 = x1;
      x1 = x2;
      x2 = p;
      h1 = x1 - x0;
      h2 = x2 - x1;
      delta1 = (f(x1) - f(x0))/h1;
      delta2 = (f(x2) - f(x1))/h2;
      d = (delta2 - delta1)/(h2 + h1);
      cont=cont+1;
end
tbl = [tbl; cont,x0,x1,x2,p,E];

T = array2table(tbl, 'VariableNames',{'i' 'x' 'x1' 'x2' 'p' 'E'});
disp(T);

%Entrega de resultados
x=p;
iter=cont;
err=E;
end
