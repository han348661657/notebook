# X-Y
fig1 = plt.figure(figsize=(9, 7))
fig1.suptitle(f'Ntimes - {nT}, N - {N}')
ax1 = fig1.add_subplot(2, 2, 1)
im1 = ax1.pcolormesh(tke1xy, cmap='jet')
fig1.colorbar(im1, ax=ax1)
ax1.set_title(f'TKE - without LC')

ax1 = fig1.add_subplot(2, 2, 2)
im1 = ax1.pcolormesh(tke2xy, cmap='jet')
fig1.colorbar(im1, ax=ax1)
ax1.set_title(f'TKE - with LC')

ax1 = fig1.add_subplot(2, 2, 3)
im1 = ax1.pcolormesh(dtke[nT, N, :, :], cmap='jet')
fig1.colorbar(im1, ax=ax1)
title3 = r'\Delta TKE'
ax1.set_title(title3)
fig1.savefig(f'figure/tke_Nt_{nT}_N_{N}.png')

fig2 = plt.figure(figsize=(9, 7))
fig2.suptitle(f'Ntimes - {nT}, N - {N}')
ax1 = fig2.add_subplot(2, 2, 1)
im1 = ax1.pcolormesh(gls1xy, cmap='jet')
fig2.colorbar(im1, ax=ax1)
ax1.set_title(f'gls - without LC')

ax1 = fig2.add_subplot(2, 2, 2)
im1 = ax1.pcolormesh(gls2xy, cmap='jet')
fig2.colorbar(im1, ax=ax1)
ax1.set_title(f'gls - with LC')

ax1 = fig2.add_subplot(2, 2, 3)
im1 = ax1.pcolormesh(dgls[nT, N, :, :], cmap='jet')
fig2.colorbar(im1, ax=ax1)
title3 = r'\Delta gls'
ax1.set_title(title3)
