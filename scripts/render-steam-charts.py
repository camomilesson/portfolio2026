"""Render portfolio figures from recorded notebook tables; does not train models.

Requires matplotlib. Run from the portfolio root:
MPLCONFIGDIR=/tmp/portfolio-mpl python scripts/render-steam-charts.py
"""
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / 'docs/dev/chart-data/steam-notebook-results.json').read_text())
OUT = ROOT / 'public/images/steam'
OUT.mkdir(parents=True, exist_ok=True)
BLUE, INK, MUTED, GRAY = '#2449e8', '#15171c', '#606672', '#dce0e7'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 11, 'axes.spines.top': False,
    'axes.spines.right': False, 'axes.spines.left': False, 'axes.edgecolor': GRAY,
    'text.color': INK, 'axes.labelcolor': MUTED, 'xtick.color': MUTED,
    'ytick.color': INK, 'svg.fonttype': 'path', 'figure.facecolor': '#ffffff',
    'axes.facecolor': '#ffffff'})

def frame(title, subtitle):
    fig, ax = plt.subplots(figsize=(12, 7.2))
    fig.subplots_adjust(left=.20, right=.91, bottom=.22, top=.72)
    fig.text(.055, .93, 'STEAM PRICE MODELING / EXPERIMENT RESULTS', fontsize=10, color=BLUE)
    fig.text(.055, .855, title, fontsize=25, weight='bold')
    fig.text(.055, .80, subtitle, fontsize=11, color=MUTED)
    ax.set_axisbelow(True)
    ax.tick_params(axis='both', length=0, pad=10)
    return fig, ax

def save(fig, name, note):
    fig.text(.055, .07, note, fontsize=9, color=MUTED, linespacing=1.6)
    for ext in ('svg', 'png'):
        path = OUT / f'{name}.{ext}'
        fig.savefig(path, dpi=150)
        if ext == 'svg':
            path.write_text('\n'.join(line.rstrip() for line in path.read_text().splitlines()) + '\n')
    plt.close(fig)

c = DATA['comparison']
fig, ax = frame('Better than a single median price',
    'Pre-release metadata · games with 10+ reviews · same 9,828-game test split')
bars = ax.barh(c['models'], c['mae_dollars'], color=[GRAY, '#9aa8cf', '#6c82c3', BLUE], height=.56)
ax.invert_yaxis()
ax.set_xlim(0, 7.2)
ax.xaxis.set_major_formatter(FuncFormatter(lambda v, _: f'${v:.0f}'))
ax.set_xlabel('Mean absolute error in dollars — lower is better', labelpad=18)
ax.grid(axis='x', color='#edf0f5')
for bar, value in zip(bars, c['mae_dollars']):
    ax.text(value+.11, bar.get_y()+bar.get_height()/2, f'${value:.3f}', va='center', weight='bold')
save(fig, 'model-comparison', 'Source: 03_modeling.ipynb, recorded selected-scope benchmarks.\nThese are notebook results; the separately tuned pipeline reports $4.554 MAE.')

s = DATA['selection']
assert s['raw_games']-s['free_games']-s['invalid_discount_games']-s['above_price_limit']==s['valid_paid_games']
fig, ax = frame('Choosing the market the model represents',
    'From the raw catalogue to a paid-game reference set with observable traction')
labels=['Raw catalogue', 'Valid paid targets', 'Selected: 10+ reviews']
values=[s['raw_games'],s['valid_paid_games'],s['selected_games']]
ax.barh(labels, values, height=.54, color=[GRAY, '#9aa8cf', BLUE])
ax.invert_yaxis(); ax.set_xlim(0,150000)
ax.xaxis.set_major_formatter(FuncFormatter(lambda v,_: f'{v/1000:.0f}k'))
ax.set_xlabel('Number of games', labelpad=18); ax.grid(axis='x',color='#edf0f5')
for i,v in enumerate(values): ax.text(v+2200,i,f'{v:,}',va='center',weight='bold')
save(fig,'data-selection','Target cleaning: 26,206 free games, 2 invalid 100% discounts, and 341 prices above $100 excluded.\n10+ reviews retains 51.2% of valid paid targets. Review count selects the cohort; it is not a launch-price feature.')

p=DATA['price_bands']
assert sum(p['counts'])==p['test_games']
fig, ax=frame('Higher prices are harder to estimate',
    'Earlier broad-market baseline experiment · full valid-price scope · 19,213 test games')
fig.subplots_adjust(left=.095,right=.96,bottom=.25)
x=list(range(len(p['bands'])))
for key,label,color,style in [('median_mae','Median baseline','#a5adbb','--'),('ridge_mae','Ridge','#7582ad','-'),('knn_mae','KNN (k=25)',BLUE,'-')]:
    ax.plot(x,p[key],marker='o',label=label,color=color,linestyle=style,linewidth=2.5)
ax.set_xticks(x,[f'{b}\nn = {n:,}' for b,n in zip(p['bands'],p['counts'])],fontsize=9)
ax.set_ylim(0,65); ax.set_ylabel('Mean absolute error ($)',labelpad=12)
ax.grid(axis='y',color='#edf0f5'); ax.legend(frameon=False,loc='upper left')
save(fig,'price-band-error','Source: 03_modeling.ipynb, cell 24. This scope differs from the lead model-comparison chart.\nOnly 127 test games fall in the highest band. These curves describe baseline models, not tuned XGBoost.')
