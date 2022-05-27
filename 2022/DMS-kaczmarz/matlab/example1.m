% EXAMPLE1  Run cyclic Kaczmarz on 3x3 example.  Formatted to help
% inclusion in slides.

N = 1000;  % total iterations

m = 3;
A = [3 1 6;
     3 -2 7;
     4 9 -3];
b = [4 2 2]';

z = A \ b;  % exact

x = zeros(3,1);

xxx = [x];
jjj = [0 1 2 3 100 200 N];
for k = 1:N
    i = mod(k-1,m) + 1
    c = (b(i) - A(i,:) * x) / (A(i,:) * A(i,:)');
    x = x + c * A(i,:)';
    if find(jjj==k),  xxx = [xxx x];  end
end
jjj
xxx
xxx'
