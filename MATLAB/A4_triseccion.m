%Este programa halla la solución a la ecuación f(x)=0 en el intervalo [a,b]
%usando el método de la trisección. 

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

%Creado por: Pascual Gómez
%última actualización: 04/04/2022
function [x,iter,err]=A4_triseccion(f,a,b,tol,Nmax)

%Inicialización
fa=f(a);
fb=f(b);
E=1000;
cont=1;

tbl = [cont,a,fa,b,fb,E];

while E>tol && cont<Nmax
    if abs(fa) < abs(fb)
        x1 = a + (b-a)/3;
        fx1 = f(x1);
        if fa*fx1 < 0
            b = x1;
            fb = fx1;
        else
            x2 = b - (b-a)/3;
            fx2 = f(x2); 
            if fx1*fx2 < 0
                a = x1;
                fa = fx1;
                b = x2;
                fb = fx2;
            else
                a = x2;
                fa = fx2;
            end
        end
    else
        x1 = b - (b-a)/3;
        fx1 = f(x1);
        if fb*fx1 < 0
            a = x1;
            fa = fx1;
        else
            x2 = a + (b-a)/3;
            fx2 = f(x2);
            if fx1*fx2 < 0
                a = x2;
                fa = fx2;
                b = x1;
                fb = fx1;
            else
                b = x2;
                fb = fx2;
            end
        end
    end
    tbl = [tbl; cont,a,fa,b,fb,E];
    E = abs(a-b);
    cont = cont + 1;
end

%Crear tabla a mostrar
T = array2table(tbl, 'VariableNames',{'i' 'a' 'f(a)' 'b' 'f(b)' 'E'});
disp(T);

x = (a+b)/2;
err = E;
iter = cont;

end