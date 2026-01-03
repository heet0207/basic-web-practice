
import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[9,7,4,5]
plt.plot(x,y,'D:r',linewidth=2,markersize=10)
# plt.plot(x,y,marker='D',color='b',linestyle=':',linewidth=2,markersize=10)
# plt.xlabel('Calories (KCAL)',fontsize=34,fontname='Comic Sans MS',color='brown',fontstyle='italic',fontweight='bold')
# plt.ylabel('Duration (s)',fontsize=34,fontname='Comic Sans MS',color='brown',fontweight='bold',fontstyle='italic')
f1={'fontsize':34,'fontname':'Comic Sans MS','color':'brown','fontstyle':'italic','fontweight':'bold'}
plt.xlabel('Calories (KCAL)',horizontalalignment='right')
plt.ylabel('Duration (s)', verticalalignment='top')
plt.title('Calories vs Duration',fontdict=f1)
plt.show()