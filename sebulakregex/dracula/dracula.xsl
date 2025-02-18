<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    exclude-result-prefixes="xs math"
    version="3.0">
    
    <xsl:mode on-no-match="shallow-copy"/>
    
    <xsl:template match="text()">
        <xsl:analyze-string select="." regex="\d.+?" flags="s">
            <!--ss: trying to isolate dates. not sure if theres a way to include months without doing it manually? also, i think i included the first digit of a few times that are mentioned. not sure how to fix that.-->
            <xsl:matching-substring>
                <date> <xsl:value-of select="regex-group(1)"/> </date>
            </xsl:matching-substring>
            
            <xsl:non-matching-substring>
                <xsl:apply-templates select="."/>
            </xsl:non-matching-substring>
<!--ss: i dont really get how this works AT ALL......-->
        </xsl:analyze-string>
    </xsl:template>
</xsl:stylesheet>