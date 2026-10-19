def maximale_blootstelling(db):
    if db < 80:
        return -1.0
    
    uren = 8 / (2**int((db-80)//3))
    return uren * 3600
    
