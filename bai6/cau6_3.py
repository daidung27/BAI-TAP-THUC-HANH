print("TONG DOAN DAI DUNG")
print("msv:24575202161009")
class Nguoi(object):
  def getGender( self ): 
      return "Unknown" 
class Nam( Nguoi ): 
  def getGender( self ): 
      return "Nam" 
class Nu( Nguoi ): 
  def getGender( self ): 
      return "Nữ" 
aNam = Nam() 
aNu= Nu() 
print (aNam.getGender()) 
print (aNu.getGender()) 
