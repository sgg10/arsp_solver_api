%EL siguiente programa realiza la sustitución regresiva a la matriz
%aumentada M=[U,b]

function x=sustregr(M)

%Inicialización
n=size(M,1);
x=zeros(n,1);

%Ciclo
x(n)=M(n,n+1)/M(n,n);
for i=n-1:-1:1
    aux=[1 x(i+1:n)'];
    aux1=[M(i,n+1) -M(i,i+1:n)];
    x(i)=dot(aux,aux1)/M(i,i);
end
end