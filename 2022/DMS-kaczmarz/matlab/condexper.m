% CONDEXPER  Generate random, square, symmetric matrices and compare
% the "progress rate factors":
%   kappa(A)^{-2}          for randomized Kaczmarz
%   2 / (sqrt(k(A)) + 1)   for conjugate gradient
% See Strohmer & Vershynin (RK) versus Greenbaum (CG) for the factors.

N = 10;       % max dimension is 2^N
S = 10;       % samples for each dimension
for q = 1:N
    n = 2^q;  % dimension
    for t = 1:S
        A = triu(randn(n,n));
        A = A + triu(A,+1)';   % symmetric with N(0,1) entries
        sig = svd(A);
        k = max(sig) / min(sig);             % = cond(A) =  |A|_2 |A^-1|_2
        kap = sqrt(sum(sig.^2)) / min(sig);  % = |A|_F |A^-1|_2
        nn(S*(q-1) + t) = n;
        cg(S*(q-1) + t) = 2.0 / (1.0 + sqrt(k));
        rk(S*(q-1) + t) = 1.0 / kap^2;
    end
end
clf
loglog(nn,cg,'bo','DisplayName','CG progress factor')
hold on
loglog(nn,rk,'k+','DisplayName','RK progress factor')
hold off
legend('Location','SouthWest')
xlabel n
axis([1 2^N 1e-9 1.0])