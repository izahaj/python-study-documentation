is_criticality_balanced = lambda t, neutrons_emitted: t < 800 and neutrons_emitted > 500 and t * neutrons_emitted < 500000


reactor_efficiency = lambda voltage,current,tmp : 'green' if (gp:= (voltage*current)/tmp*100) >= 80 else 'orange' if gp >= 60 else 'red' if gp >= 30 else 'black'


fail_safe = lambda t, nps, threshold: 'LOW' if (c:= t * nps) < 0.9 * threshold else 'NORMAL' if 0.9 * threshold <= c <= 1.1 * threshold else 'DANGER'

    