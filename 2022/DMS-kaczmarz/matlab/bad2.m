% BAD2  in support of a slide

A = [5 -1; 6 -1]
cond(A)
b = [1 2]'
xstar = [1 4]'  % exact

x = [-3 -3]';
for n = 1:4000
    err(2*n-1) = norm(x - xstar);
    x = x + ((b(1) - A(1,:) * x) / norm(A(1,:))^2) * A(1,:)';
    err(2*n) = norm(x - xstar);
    x = x + ((b(2) - A(2,:) * x) / norm(A(2,:))^2) * A(2,:)';
end

max(err)
min(err)
semilogy(1:8000,err,'.')
xlabel('k','FontSize',14)
ylabel('error','FontSize',14)
