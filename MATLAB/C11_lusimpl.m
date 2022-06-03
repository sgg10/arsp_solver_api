%Este programa halla la solución al sistema Ax=b y la factorización LU de A
%usando el método de factorización LU con eliminación gaussiana simple.  

%Entradas: 
%A, matrix invertible
%b, vector constante

%Salidas
%x, solución
%L, matriz L de la factorización
%U, matriz U de la factorización

%Creado por: Samir Posada
%última actualización: 16/07/2020

function [x,L,U]=C11_lusimpl(A,b)

file=fopen('lusimple.txt','w')

if det(A) == 0
    disp("Error: Det(A) = 0");
    fprintf(fileID,'%s\r\n',"Error: Det(A) = 0"); % Genera la primera línea
    x = NaN;
    M = NaN;
    return
end

%Inicialización
n=size(A,1);
L=eye(n);
U=zeros(n);
M=A;

for i=1:n
    if A(i,i) == 0
        disp("Error: A has ceros in its diagonal.");
        fprintf(fileID,'%s\r\n',"Error: A has ceros in its diagonal."); % Genera la primera línea
        x = NaN;
        L = NaN;
        U = NaN;
    return
    end

end

%Factorización
for i=1:n-1
    for j=i+1:n
        if M(j,i)~=0
           L(j,i)=M(j,i)/M(i,i);
           M(j,i:n)=M(j,i:n)-(M(j,i)/M(i,i))*M(i,i:n);           
        end
    end
    U(i,i:n)=M(i,i:n);
    U(i+1,i+1:n)=M(i+1,i+1:n);
    
    fprintf(file,'Etapa %u\n',i);
    fprintf(file,'\nL:\n');
    fprintf(file,[repmat(' %.6f ',1,n) '\n'], L');
    fprintf(file,'\nU:\n');
    fprintf(file,[repmat(' %.6f ',1,n) '\n'], U');
    fprintf(file,'\n');
end
U(n,n)=M(n,n);

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
