%Este programa halla la solución al sistema Ax=b y la factorización LU de A
%usando el método de Cholesky

%Entradas: 
%A, matrix invertible
%b, vector constante

%Salidas
%x, solución
%L, matriz L de la factorización
%U, matriz U de la factorización

%Creado por: Samir Posada
%última actualización: 16/07/2020

function [x,L,U]=C15_Cholesky(A,b)

file=fopen('cholesky.txt','w')

%Inicialización
n=size(A,1);
L=eye(n); 
U=eye(n);

%Factorización
for i=1:n-1
    if A(i,i)-dot(L(i,1:i-1),U(1:i-1,i)') < 0
        fprintf(file,"Root square of a negative value. Complex numbers not supported.\n");
    end
    L(i,i)=sqrt(A(i,i)-dot(L(i,1:i-1),U(1:i-1,i)'));
    U(i,i)=L(i,i);
    for j=i+1:n
        L(j,i)=(A(j,i)-dot(L(j,1:i-1),U(1:i-1,i)'))/U(i,i);
    end
    for j=i+1:n
        U(i,j)=(A(i,j)-dot(L(i,1:i-1),U(1:i-1,j)'))/L(i,i);
    end
    fprintf(file,'Etapa %u\n',i);
    fprintf(file,'\nL:\n');
    fprintf(file,[repmat(' %.6f ',1,n) '\n'], L');
    fprintf(file,'\nU:\n');
    fprintf(file,[repmat(' %.6f ',1,n) '\n'], U');
    fprintf(file,'\n');
end
if A(n,n)-dot(L(n,1:n-1),U(1:n-1,n)') < 0
        fprintf(file,"Root square of a negative value. Complex numbers not supported.\n");
end
L(n,n)=sqrt(A(n,n)-dot(L(n,1:n-1),U(1:n-1,n)'));
U(n,n)=L(n,n);

fprintf(file,'Etapa %u\n',i+1);
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