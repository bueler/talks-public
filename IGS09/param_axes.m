% runs in Matlab *not* octave
% some rotation and label shifts needed to get param_axes.png

figure(1)

plot3(0,0,0,'k.','markersize',35)
hold on
text(-0.1,0.1,0,'control','color','k','fontsize',12)

plot3([0 1],[0 0],[0 0],'r','linewidth',4.0)
plot3([0 -1],[0 0],[0 0],'r','linewidth',2.0)
plot3(1,0,0,'r.','markersize',30)
plot3(-1,0,0,'r.','markersize',30)
text(1.2,0,0,'higher enhancement','color','r','fontsize',12)
text(-1.2,0,0,'lower enhancement','color','r','fontsize',12)

plot3([0 0],[0 1],[0 0],'color',[0 0.6 0],'linewidth',4.0)
plot3([0 0],[0 -1],[0 0],'color',[0 0.6 0],'linewidth',2.0)
plot3(0,1,0,'.','markersize',30,'color',[0 0.6 0])
plot3(0,-1,0,'.','markersize',30,'color',[0 0.6 0])
text(0,1.2,0,'plastic-ish till','color',[0 0.6 0],'fontsize',12,'FontWeight','bold')
text(0,-1.2,0.1,'linear-ish till','color',[0 0.6 0],'fontsize',12,'FontWeight','bold')

plot3([0 0],[0 0],[0 1],'b','linewidth',4.0)
plot3([0 0],[0 0],[0 -1],'b','linewidth',2.0)
plot3(0,0,1,'b.','markersize',30)
plot3(0,0,-1,'b.','markersize',30)
text(0,0,1.2,'higher pore pressure','color','b','fontsize',12)
text(0,0,-1.2,'lower pore pressure','color','b','fontsize',12)

plot3(0,0,0,'k.','markersize',35)

hold off
axis off


% one axis at a time figures:
themecolor=[[1 0 0]
            [0 0.6 0]
            [0 0 1]];
endslabels= ...
     [{'  higher enhancement', 'lower enhancement  '} 
      {'    plastic-ish till', 'linear-ish till    '} 
      {'higher pore pressure', 'lower pore pressure'}];
for n=1:3
  figure(n+1)
  plot([0 1],[0 0],'color',themecolor(n,:),'linewidth',4.0)
  hold on
  plot([-1 0],[0 0],'color',themecolor(n,:),'linewidth',2.0)
  plot(1,0,'.','color',themecolor(n,:),'markersize',30)
  plot(-1,0,'.','color',themecolor(n,:),'markersize',30)
  text(0.4,0.2,endslabels(n,1),'color',themecolor(n,:),'fontsize',12)
  text(-1,0.2,endslabels(n,2),'color',themecolor(n,:),'fontsize',12)
  plot(0,0,'k.','markersize',35)
  text(-0.1,0.2,'control','color','k','fontsize',12)
  hold off
  axis off
end
