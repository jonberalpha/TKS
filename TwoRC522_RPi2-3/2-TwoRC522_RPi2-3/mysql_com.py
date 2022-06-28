import MySQLdb
import os

def mysqlinsertstarttime(chipid):
    db = MySQLdb.connect("localhost", "pi", "****", "****")
    curs = db.cursor()

    try:
        query = "SELECT Nr FROM eventdata WHERE ChipID = '{}';".format(chipid)
        curs.execute(query)
        result = curs.fetchone()
        if result: #if the chip exists
            query = "SELECT Startzeit FROM eventdata WHERE ChipID = '{}';".format(chipid)
            curs.execute(query)
            result = curs.fetchone()
            if result[0] is None: #only if time not exists write time
                query = "UPDATE eventdata SET Startzeit = CURTIME(2) WHERE ChipID = '{}';".format(chipid)
                curs.execute(query)
                db.commit()
                print "Startzeit von dem Chip " + chipid + " eingetragen!"
                execfile("/home/pi/Bierrallye/ZMS_python/piezo1.py") # piezo
        else: #if the chip does not exist, add it
            query = "SELECT ChipNum FROM chipdata WHERE ChipID =  '{}';".format(chipid)
            curs.execute(query)
            result = curs.fetchone()
            if result[0] is not None:
                query = "INSERT INTO eventdata (ChipNum,ChipID,Startzeit) VALUES ({},'{}',CURTIME(2));".format(result[0],chipid)
                curs.execute(query)
                db.commit()
                print "Startzeit von unbekannten Chip " + chipid + " eingetragen!"
                execfile("/home/pi/Bierrallye/ZMS_python/piezo1.py") # piezo
            else:
                print "ChipID " + chipid + " is not listed!"
        db.close()
    except:
        print "Error. Rolling back..."
        db.rollback()
        db.close()

def mysqlinsertstoptime(chipid):
    db = MySQLdb.connect("localhost", "pi", "****", "****")
    curs = db.cursor()

    try:
        query = "SELECT Nr FROM eventdata WHERE ChipID = '{}';".format(chipid)
        curs.execute(query)
        result = curs.fetchone()
        if result: #if the chip exists
            query = "SELECT Endzeit FROM eventdata WHERE ChipID = '{}';".format(chipid)
            curs.execute(query)
            result = curs.fetchone()
            if result[0] is None: #only if time not exists write time
                query = "UPDATE eventdata SET Endzeit = CURTIME(2) WHERE ChipID = '{}';".format(chipid)
                curs.execute(query)
                db.commit()
                print "Endzeit von dem Chip " + chipid + " eingetragen!"
                mysqlinsertruntime(chipid)
        else: #if the chip does not exist, add it
            query = "SELECT ChipNum FROM chipdata WHERE ChipID =  '{}';".format(chipid)
            curs.execute(query)
            result = curs.fetchone()
            if result[0] is not None:
                query = "INSERT INTO eventdata (ChipNum,ChipID,Endzeit) VALUES ({},'{}',CURTIME(2));".format(result[0],chipid)
                curs.execute(query)
                db.commit()
                print "Endzeit von dem unbekannten Chip " + chipid + " eingetragen!"
                execfile("/home/pi/Bierrallye/ZMS_python/piezo2.py") # piezo
            else:
                print "ChipID " + chipid + " is not listed!"
        db.close()
    except:
        print "Error. Rolling back..."
        db.rollback()
        db.close()
        
def mysqlinsertruntime(chipid):
    db = MySQLdb.connect("localhost", "pi", "****", "****")
    curs = db.cursor()

    try:
        query = "UPDATE eventdata SET Laufzeit = TIMEDIFF(Endzeit,Startzeit) WHERE ChipID='{}';".format(chipid)
        curs.execute(query)
        db.commit()
        db.close()
        print "Laufzeit von dem Chip " + chipid + " eingetragen!"
        execfile("/home/pi/Bierrallye/ZMS_python/piezo2.py") # piezo
    except:
        print "Error. Rolling back..."
        db.rollback()
        db.close()
