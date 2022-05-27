% KACZ   Test out Kaczmarz iteration.

% FIXME try randomization

n = 4;
K = 200;

A = randn(n,n);
b = randn(n,1);

x = zeros(n,1);
for j = 1:K
    i = mod(j - 1,n) + 1;
    fprintf('j = %2d, i = %2d:  %.3e\n', j, i, norm(A*x - b));
    c = (b(i) - A(i,:) * x) / (A(i,:) * A(i,:)');
    x = x + c * A(i,:)';
end
