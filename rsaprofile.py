import os
import commands
import re
import  xml.etree.ElementTree as Etree
import  StringIO

def provisioningshowxml(filename):
    currentpath = os.getcwd()
    usr_home = os.path.expanduser('~')
    os.chdir(usr_home + '/Library/MobileDevice/Provisioning Profiles')
    status,output = commands.getstatusoutput(' openssl smime -in '+filename+' -inform der -verify')
    print output
    os.chdir(currentpath)
    if status == 0:
        output = output.replace('Verification successful\n','')
        root = Etree.parse(StringIO.StringIO(output)).getroot()
        for dict in root:
            for index,item in enumerate(dict):
            	print 'item:',dict[index+1].text
                if item.text == 'Name':
                    value = dict[index+1].text
                    return (value,usr_home + '/Library/MobileDevice/Provisioning Profiles/'+filename)
    else:
        common.log('error:provisioning file uncode faild')
if __name__ == "__main__":
	out =  provisioningshowxml('/Users/tinkl/Library/MobileDevice/Provisioning\ Profiles/5d48ead5-55ae-43db-9fd8-7bf1426b437a.mobileprovision')
	print out
	#8bf22619-1a07-40b5-b0d6-856404712a28 5d48ead5-55ae-43db-9fd8-7bf1426b437a