import subprocess
import paho.mqtt.publish as publish
import ast

proc = subprocess.Popen(['./bsec_bme680'], stdout=subprocess.PIPE)

for line in iter( proc.stdout.readline, '' ):
    line_str = str( line )
    line_str = line_str.replace( 'b\'', '' )
    line_str = line_str.replace( '\\r\\n\'', '' )
    value = ast.literal_eval( line_str )

    print( "IAQ : {}".format( value["IAQ"] ) )

