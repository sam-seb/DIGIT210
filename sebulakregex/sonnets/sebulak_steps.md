# Sonnet Regex

Find: ``&``, ``<``, and ``>``  
Replace:``&amp;``, ``&lt:`` ``&gt:``, respectively

Find: ^X+  
Replace: delete them

Find: ``\n+``  
Replace: ``\n``

Find: ^.+  
Replace:``<line>\0</line>``

Find: ``(<line>)([IVXLC]+)(</line>)``  
Replace: ``</sonnet><sonnet number="\2">``

Add xml start and end tags