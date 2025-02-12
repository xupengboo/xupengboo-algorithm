msg = "123123"
body2 = {"mod:in0", f'<![CDATA[{msg}]]>'}
body = {"mod:saveModeData": body2}
print(body)