%Este programa halla el spline lineal que interpola los datos dados usando el
%m�todo de trazadores lineales

%Entradas: 
%X, abscisas 
%Y, ordenadas

%Salidas
%Coef, coeficientes de los trazadores

%Creado por: Samir Posada
%�ltima actualizaci�n: 16/07/2020

function [Coef,A,b,M]=C22_trazlin(X,Y)

file=fopen('trazlin.txt','w');


%Inicializaci�n
n=length(X);
m=2*(n-1);
A=zeros(m); 
b=zeros(m,1);
Coef=zeros(n-1,2);
M = [];

%Ciclos
%Condiciones de interpolaci�n
for i=1:length(X)-1
    A(i+1,[2*i-1 2*i])=[X(i+1) 1];
    b(i+1)=Y(i+1);
end
A(1,[1 2])=[X(1) 1];
b(1)=Y(1);
%Condiciones de continuidad
for i=2:length(X)-1
    A(length(X)-1+i,2*i-3:2*i)=[X(i) 1 -X(i) -1];
    b(length(X)-1+i)=0;
end   

fprintf(file,'\nA:\n');
fprintf(file,[repmat(' %.6f ',1,length(A(1,:))) '\n'], A');

%Entrega de resultados
Saux=A\b;
% [Saux,M]=C8_gausspl(A,b)
% [Saux,M]=C9_gausspar(A,b)
% [Saux,M]=C10_gausstot(A,b)
%Se organiza la matriz de salida
for i=1:length(X)-1
    Coef(i,:)=Saux([2*i-1 2*i]);
end
fprintf(file,'\nCoef:\n');
fprintf(file,[repmat(' %.6f ',1,length(Coef(1,:))) '\n'], Coef');

fprintf(file,'\nSplines:\n');
lrow = length(Coef(:,1));
lcol = length(Coef(1,:));
for i=1:lrow
    count = lcol-1;
    for j=1:lcol
        fprintf(file,' %.6f',Coef(i,j));
        fprintf(file,'*x^%u ',count);
        if count-1 >= 0
            fprintf(file,' + ');
        end
        count = count - 1;
    end
    fprintf(file,'\n');
end
end