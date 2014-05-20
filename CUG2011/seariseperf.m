% SEARISEPERF  graph searise 100 model year run performance as weak-scaling
%              data was hand assembled from "count_time_steps" and "average dt"
%              in stdout files searise_N.out and in "wall clock hours" from
%              history string in gDXkm_N_pre100.nc; all of these are from pacman
%              runs in r1729

set(0,'defaultaxesfontsize',14)

N = [1 4 16 64 256]; % number of processors
Nlabels = {'1','4','16','64','256'};
Nlim = [0.8 280];

DX = [40 20 10 5 2.5]; % km
DXlabels_reverse = {'2.5','5','10','20','40'}; % matlab (but not octave) needs increasing x for loglog

dt = [1.408 0.3257 0.06192 0.01366 0.002982];  % years
steps = [71 307 1615 7321 33529];
time_hrs = [0.0057 0.0226 0.1215 0.8568 4.5522];

for fn=1:2
  figure(fn)
  if fn==1
    semilogx(N,time_hrs*3600,'ks','markersize',12,'MarkerFaceColor','g')
    ylabel('wall clock time  (seconds)')
    axis([Nlim [0 1.1*max(time_hrs*3600)]])
  elseif fn==2
    semilogx(N,(time_hrs./steps)*3600,'ks','markersize',12,'MarkerFaceColor','g')
    ylabel('time per step  (seconds)')
    axis([Nlim [0 1.1*max((time_hrs./steps)*3600)]])
  else, error('no case here'), end
  xlabel('processors')
  set(gca,'xtick',N)
  set(gca,'xticklabel',Nlabels)
end

figure(3)
loglog(DX(5:-1:1),dt(5:-1:1),'.','markersize',20)
xlabel('\Delta x  (km)'), ylabel('\Delta t  (model years)')
set(gca,'xtick',DX(5:-1:1))
set(gca,'xticklabel',DXlabels_reverse)
p=polyfit(log(DX(5:-1:1)),log(dt(5:-1:1)),1)
hold on
loglog(DX(5:-1:1),exp(p(2))*exp(p(1)*log(DX(5:-1:1))),'r:')
legend('data',['\Delta t \sim {\Delta x}^{ ' num2str(p(1)) '}'],...
       'Location','NorthWest')
hold off
axis([2 60 0.001 2])

figure(1), print -dpdf weak-time.pdf
figure(2), print -dpdf weak-time-per-step.pdf
figure(3), print -dpdf dt-dx-power.pdf

return

figure(4)
loglog(N,time_hrs,'.','markersize',20)
q = polyfit(log(N),log(time_hrs),1);
xlabel('processors'), ylabel('wall clock time (hours)')
set(gca,'xtick',N)
set(gca,'xticklabel',Nlabels)
hold on
loglog(N,exp(q(2))*exp(q(1)*log(N)),'r:')
legend('data',['(wall clock time) \sim N^{ ' num2str(q(1)) '}'],...
       'Location','NorthWest')
hold off

