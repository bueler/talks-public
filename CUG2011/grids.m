% generate grids to show scaling definitions

ii = repmat((1:4)',1,4);
jj = repmat(1:4,4,1);
colors = {'r.', 'g.', 'b.', 'm.'};
dotsize = 30;
arrowwidth = 2.5;

for fn=1:2
  figure(fn), clf, hold on

  % right plot
  ox = 6; oy = 0;
  % black thin lines
  for i=1:4, plot(ii(:,i)+ox,jj(:,i)+oy,'k'), end
  for j=1:4, plot(ii(j,:)+ox,jj(j,:)+oy,'k'), end
  % big colored grid points
  plot(ii(1:2,1:2)+ox,jj(1:2,1:2)+oy,char(colors(1,1)),'markersize',dotsize)
  plot(ii(1:2,3:4)+ox,jj(1:2,3:4)+oy,char(colors(1,2)),'markersize',dotsize)
  plot(ii(3:4,1:2)+ox,jj(3:4,1:2)+oy,char(colors(1,3)),'markersize',dotsize)
  plot(ii(3:4,3:4)+ox,jj(3:4,3:4)+oy,char(colors(1,4)),'markersize',dotsize)    

  % arrows
  plot([4.5 6.5],[2.5 2.5],'k','linewidth',arrowwidth)
  plot([6.3 6.5],[2.69 2.49],'k','linewidth',arrowwidth)
  plot([6.3 6.5],[2.31 2.51],'k','linewidth',arrowwidth)

  % left plots
  ox = 0; oy = 0;
  if fn==1
    % strong case
    % black thin lines
    for i=1:4, plot(ii(:,i)+ox,jj(:,i)+oy,'k'), end
    for j=1:4, plot(ii(j,:)+ox,jj(j,:)+oy,'k'), end
    % big colored grid points
    plot(ii(:,:)+ox,jj(:,:)+oy,char(colors(1,1)),'markersize',dotsize)
  else
    % weak case
    % black thin lines
    for i=[1 4], plot(ii([1 4],i)+ox,jj([1 4],i)+oy,'k'), end
    for j=[1 4], plot(ii(j,[1 4])+ox,jj(j,[1 4])+oy,'k'), end
    % big colored grid points
    plot(ii([1 4],[1 4])+ox,jj([1 4],[1 4])+oy,char(colors(1,1)),'markersize',dotsize)
  end

  axis([0 11 0 5])
  axis off
  axis equal
  hold off
end
