%Este programa halla la solución al sistema Ax=b y la factorización LU de PA
%usando el método de factorización LU con eliminación gaussiana con pivoteo parcial.  

%Entradas: 
%A, matrix invertible
%b, vector constante

%Salidas
%x, solución
%L, matriz L de la factorización
%U, matriz U de la factorización
%P, matriz de permutación

%Creado por: Samir Posada
%última actualización: 16/07/2020

function [x,L,U,P]=C12_lupar(A,b)

file=fopen('lupar.txt','w')

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
P=eye(n);
M=A;

%Factorización
for i=1:n-1
    %Cambio de filas
    [aux0,aux]=max(abs(M(i+1:n,i)))
    M(i+1:n,i)
    if aux0>abs(M(i,i))
        aux2=M(i+aux,i:n);
        aux3=P(i+aux,:);
        M(aux+i,i:n)=M(i,i:n);
        P(aux+i,:)=P(i,:);
        M(i,i:n)=aux2;
        P(i,:)=aux3;
        if i>1
           aux4=L(i+aux,1:i-1);
           L(i+aux,1:i-1)=L(i,1:i-1);
           L(i,1:i-1)=aux4;
        end
    end
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
z=sustprgr([L P*b]);
x=sustregr([U z]);

fprintf(file,'\nz:\n');
fprintf(file,[repmat(' %.6f ',1,n) '\n'], z);
fprintf(file,'\n');
fprintf(file,'\nx:\n');
fprintf(file,[repmat(' %.6f ',1,n) '\n'], x);
fprintf(file,'\n');
end