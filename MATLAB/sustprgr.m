%EL siguiente programa realiza la sustitución progresiva a la matriz
%aumentada M=[L,b]

function x=sustprgr(M)

%Inicialización
n=size(M,1);
x=zeros(n,1);

%Ciclo
x(1)=M(1,n+1)/M(1,1);
for i=2:n
    aux=[1 x(1:i-1)'];
    aux1=[M(i,n+1) -M(i,1:i-1)];
    x(i)=dot(aux,aux1)/M(i,i);
end
end