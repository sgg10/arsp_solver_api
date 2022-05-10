%Este programa halla la soluci�n al sistema Ax=b y la factorizaci�n LU de A
%usando el m�todo de Crout

%Entradas: 
%A, matrix invertible
%b, vector constante

%Salidas
%x, soluci�n
%L, matriz L de la factorizaci�n
%U, matriz U de la factorizaci�n

%Creado por: Samir Posada
%�ltima actualizaci�n: 16/07/2020

function [x,L,U]=C13_Crout(A,b)

file=fopen('crout.txt','w')

%Inicializaci�n
n=size(A,1);
L=eye(n); 
U=eye(n);

%Revisar que la matriz sea cuadrada
%Revisar que la dimesión de b sea igual al número de filas

%Factorizaci�n
for i=1:n-1
    for j=i:n
        L(j,i)=A(j,i)-dot(L(j,1:i-1),U(1:i-1,i)');
    end
    for j=i+1:n
        U(i,j)=(A(i,j)-dot(L(i,1:i-1),U(1:i-1,j)'))/L(i,i);
    end
    fprintf(file,'Etapa %u\n\n',i);
    fprintf(file,'\nL:\n');
    fprintf(file,[repmat(' %.6f ',1,n) '\n'], L');
    fprintf(file,'\nU:\n');
    fprintf(file,[repmat(' %.6f ',1,n) '\n'], U');
    fprintf(file,'\n');
end
L(n,n)=A(n,n)-dot(L(n,1:n-1),U(1:n-1,n)');

fprintf(file,'Etapa %u\n\n',i+1);
fprintf(file,'\nL:\n');
fprintf(file,[repmat(' %.6f ',1,n) '\n'], L');
fprintf(file,'\nU:\n');
fprintf(file,[repmat(' %.6f ',1,n) '\n'], U');
fprintf(file,'\n');

%Entrega de resultados
z=sustprgr([L b]);
x=sustregr([U z]);   

fprintf(file,'\nz:\n');
fprintf(file,[repmat(' %.6f ',1,n) '\n'], z);
fprintf(file,'\n');
fprintf(file,'\nx:\n');
fprintf(file,[repmat(' %.6f ',1,n) '\n'], x);
fprintf(file,'\n');
end