% GREENLANDBOXES  I could not find this famous figure, so I recreated it.
% The source of the first 10 data boxes is in
%    A. Shepherd and D. Wingham (2007), "Recent sea-level contributions of the
%    Antarctic and Greenland ice sheets," Science 315, 1529--1532
%    doi 10.1126/science.1136776
% The last box is
%    I. Velicogna (2009), "Increasing rates of ice mass loss from the Greenland
%    and Antarctic ice sheets revealed by GRACE," Geophys. Res. Let. 36, L19503,
%    doi:10.1029/2009GL040222


X = [{'Krabill et al. (2000)',           1993,1999, -47, 2}; 
     {'Velicogna and Wahr (2005)  G',    2002,2004, -75,21};
     {'Zwally et al. (2005)',            1992,2002,  11, 3};
     {'Zwally et al. (2005)',            1996,1997, -83,28};
     {'Rignot and Kanagartnam (2006)',   2000,2001,-127,28};
     {'Rignot and Kanagartnam (2006)',   2005,2006,-205,28};
     {'Ramillien et al. (2006)',         2002,2005,-169,66};
     {'Velicogna and Wahr (2006)  G',    2002,2006,-227,33};
     {'Chen et al. (2006)  G',           2002,2005,-219,21};
     {'Luthcke et al. (2006)  G',        2003,2005,-101,16};
     {'Velicogna (2009)  G',             2002,2009,-230,33}];

CC = jet;
N = size(X,1);  % = 11

for j=1:N
  boxx = [X{j,2} X{j,3} X{j,3} X{j,2} X{j,2}];
  b = X{j,4}-X{j,5};
  t = X{j,4}+X{j,5};
  boxy = [b b t t b];
  h = fill(boxx,boxy,'k');
  hold on
  set(h,'facecolor',CC(j*5,:))
  set(h,'facealpha',0.35)
end
grid on
axis([1992 2010 -280 50])
xlabel('year')
ylabel('Gt year^{-1}')
hold off
legend(X{:,1})

print -dpng -r130 foo.png


