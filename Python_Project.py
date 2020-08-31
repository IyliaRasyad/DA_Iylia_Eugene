import pandas as pd
import matplotlib.pyplot as plt

ListOfData = pd.read_csv('IMVA2.csv', skiprows=[33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62])

# removing irrelevant data
date = '1978 Jan'
del ListOfData[date]
date = '1978 Feb'
del ListOfData[date]
date = '1978 Mar'
del ListOfData[date]
date = '1978 Apr'
del ListOfData[date]
date = '1978 May'
del ListOfData[date]
date = '1978 Jun'
del ListOfData[date]
date = '1978 Jul'
del ListOfData[date]
date = '1978 Aug'
del ListOfData[date]
date = '1978 Sep'
del ListOfData[date]
date = '1978 Oct'
del ListOfData[date]
date = '1978 Nov'
del ListOfData[date]
date = '1978 Dec'
del ListOfData[date]

date = '1979 Jan'
del ListOfData[date]
date = '1979 Feb'
del ListOfData[date]
date = '1979 Mar'
del ListOfData[date]
date = '1979 Apr'
del ListOfData[date]
date = '1979 May'
del ListOfData[date]
date = '1979 Jun'
del ListOfData[date]
date = '1979 Jul'
del ListOfData[date]
date = '1979 Aug'
del ListOfData[date]
date = '1979 Sep'
del ListOfData[date]
date = '1979 Oct'
del ListOfData[date]
date = '1979 Nov'
del ListOfData[date]
date = '1979 Dec'
del ListOfData[date]

date = '1980 Jan'
del ListOfData[date]
date = '1980 Feb'
del ListOfData[date]
date = '1980 Mar'
del ListOfData[date]
date = '1980 Apr'
del ListOfData[date]
date = '1980 May'
del ListOfData[date]
date = '1980 Jun'
del ListOfData[date]
date = '1980 Jul'
del ListOfData[date]
date = '1980 Aug'
del ListOfData[date]
date = '1980 Sep'
del ListOfData[date]
date = '1980 Oct'
del ListOfData[date]
date = '1980 Nov'
del ListOfData[date]
date = '1980 Dec'
del ListOfData[date]

date = '1981 Jan'
del ListOfData[date]
date = '1981 Feb'
del ListOfData[date]
date = '1981 Mar'
del ListOfData[date]
date = '1981 Apr'
del ListOfData[date]
date = '1981 May'
del ListOfData[date]
date = '1981 Jun'
del ListOfData[date]
date = '1981 Jul'
del ListOfData[date]
date = '1981 Aug'
del ListOfData[date]
date = '1981 Sep'
del ListOfData[date]
date = '1981 Oct'
del ListOfData[date]
date = '1981 Nov'
del ListOfData[date]
date = '1981 Dec'
del ListOfData[date]

date = '1982 Jan'
del ListOfData[date]
date = '1982 Feb'
del ListOfData[date]
date = '1982 Mar'
del ListOfData[date]
date = '1982 Apr'
del ListOfData[date]
date = '1982 May'
del ListOfData[date]
date = '1982 Jun'
del ListOfData[date]
date = '1982 Jul'
del ListOfData[date]
date = '1982 Aug'
del ListOfData[date]
date = '1982 Sep'
del ListOfData[date]
date = '1982 Oct'
del ListOfData[date]
date = '1982 Nov'
del ListOfData[date]
date = '1982 Dec'
del ListOfData[date]

date = '1983 Jan'
del ListOfData[date]
date = '1983 Feb'
del ListOfData[date]
date = '1983 Mar'
del ListOfData[date]
date = '1983 Apr'
del ListOfData[date]
date = '1983 May'
del ListOfData[date]
date = '1983 Jun'
del ListOfData[date]
date = '1983 Jul'
del ListOfData[date]
date = '1983 Aug'
del ListOfData[date]
date = '1983 Sep'
del ListOfData[date]
date = '1983 Oct'
del ListOfData[date]
date = '1983 Nov'
del ListOfData[date]
date = '1983 Dec'
del ListOfData[date]

date = '1984 Jan'
del ListOfData[date]
date = '1984 Feb'
del ListOfData[date]
date = '1984 Mar'
del ListOfData[date]
date = '1984 Apr'
del ListOfData[date]
date = '1984 May'
del ListOfData[date]
date = '1984 Jun'
del ListOfData[date]
date = '1984 Jul'
del ListOfData[date]
date = '1984 Aug'
del ListOfData[date]
date = '1984 Sep'
del ListOfData[date]
date = '1984 Oct'
del ListOfData[date]
date = '1984 Nov'
del ListOfData[date]
date = '1984 Dec'
del ListOfData[date]

date = '1985 Jan'
del ListOfData[date]
date = '1985 Feb'
del ListOfData[date]
date = '1985 Mar'
del ListOfData[date]
date = '1985 Apr'
del ListOfData[date]
date = '1985 May'
del ListOfData[date]
date = '1985 Jun'
del ListOfData[date]
date = '1985 Jul'
del ListOfData[date]
date = '1985 Aug'
del ListOfData[date]
date = '1985 Sep'
del ListOfData[date]
date = '1985 Oct'
del ListOfData[date]
date = '1985 Nov'
del ListOfData[date]
date = '1985 Dec'
del ListOfData[date]

date = '1986 Jan'
del ListOfData[date]
date = '1986 Feb'
del ListOfData[date]
date = '1986 Mar'
del ListOfData[date]
date = '1986 Apr'
del ListOfData[date]
date = '1986 May'
del ListOfData[date]
date = '1986 Jun'
del ListOfData[date]
date = '1986 Jul'
del ListOfData[date]
date = '1986 Aug'
del ListOfData[date]
date = '1986 Sep'
del ListOfData[date]
date = '1986 Oct'
del ListOfData[date]
date = '1986 Nov'
del ListOfData[date]
date = '1986 Dec'
del ListOfData[date]

date = '1987 Jan'
del ListOfData[date]
date = '1987 Feb'
del ListOfData[date]
date = '1987 Mar'
del ListOfData[date]
date = '1987 Apr'
del ListOfData[date]
date = '1987 May'
del ListOfData[date]
date = '1987 Jun'
del ListOfData[date]
date = '1987 Jul'
del ListOfData[date]
date = '1987 Aug'
del ListOfData[date]
date = '1987 Sep'
del ListOfData[date]
date = '1987 Oct'
del ListOfData[date]
date = '1987 Nov'
del ListOfData[date]
date = '1987 Dec'
del ListOfData[date]
# 1988 - 1997 is for checking purposes

date = '1998 Jan'
del ListOfData[date]
date = '1998 Feb'
del ListOfData[date]
date = '1998 Mar'
del ListOfData[date]
date = '1998 Apr'
del ListOfData[date]
date = '1998 May'
del ListOfData[date]
date = '1998 Jun'
del ListOfData[date]
date = '1998 Jul'
del ListOfData[date]
date = '1998 Aug'
del ListOfData[date]
date = '1998 Sep'
del ListOfData[date]
date = '1998 Oct'
del ListOfData[date]
date = '1998 Nov'
del ListOfData[date]
date = '1998 Dec'
del ListOfData[date]

date = '1999 Jan'
del ListOfData[date]
date = '1999 Feb'
del ListOfData[date]
date = '1999 Mar'
del ListOfData[date]
date = '1999 Apr'
del ListOfData[date]
date = '1999 May'
del ListOfData[date]
date = '1999 Jun'
del ListOfData[date]
date = '1999 Jul'
del ListOfData[date]
date = '1999 Aug'
del ListOfData[date]
date = '1999 Sep'
del ListOfData[date]
date = '1999 Oct'
del ListOfData[date]
date = '1999 Nov'
del ListOfData[date]
date = '1999 Dec'
del ListOfData[date]

date = '2000 Jan'
del ListOfData[date]
date = '2000 Feb'
del ListOfData[date]
date = '2000 Mar'
del ListOfData[date]
date = '2000 Apr'
del ListOfData[date]
date = '2000 May'
del ListOfData[date]
date = '2000 Jun'
del ListOfData[date]
date = '2000 Jul'
del ListOfData[date]
date = '2000 Aug'
del ListOfData[date]
date = '2000 Sep'
del ListOfData[date]
date = '2000 Oct'
del ListOfData[date]
date = '2000 Nov'
del ListOfData[date]
date = '2000 Dec'
del ListOfData[date]

date = '2001 Jan'
del ListOfData[date]
date = '2001 Feb'
del ListOfData[date]
date = '2001 Mar'
del ListOfData[date]
date = '2001 Apr'
del ListOfData[date]
date = '2001 May'
del ListOfData[date]
date = '2001 Jun'
del ListOfData[date]
date = '2001 Jul'
del ListOfData[date]
date = '2001 Aug'
del ListOfData[date]
date = '2001 Sep'
del ListOfData[date]
date = '2001 Oct'
del ListOfData[date]
date = '2001 Nov'
del ListOfData[date]
date = '2001 Dec'
del ListOfData[date]

date = '2002 Jan'
del ListOfData[date]
date = '2002 Feb'
del ListOfData[date]
date = '2002 Mar'
del ListOfData[date]
date = '2002 Apr'
del ListOfData[date]
date = '2002 May'
del ListOfData[date]
date = '2002 Jun'
del ListOfData[date]
date = '2002 Jul'
del ListOfData[date]
date = '2002 Aug'
del ListOfData[date]
date = '2002 Sep'
del ListOfData[date]
date = '2002 Oct'
del ListOfData[date]
date = '2002 Nov'
del ListOfData[date]
date = '2002 Dec'
del ListOfData[date]

date = '2003 Jan'
del ListOfData[date]
date = '2003 Feb'
del ListOfData[date]
date = '2003 Mar'
del ListOfData[date]
date = '2003 Apr'
del ListOfData[date]
date = '2003 May'
del ListOfData[date]
date = '2003 Jun'
del ListOfData[date]
date = '2003 Jul'
del ListOfData[date]
date = '2003 Aug'
del ListOfData[date]
date = '2003 Sep'
del ListOfData[date]
date = '2003 Oct'
del ListOfData[date]
date = '2003 Nov'
del ListOfData[date]
date = '2003 Dec'
del ListOfData[date]

date = '2004 Jan'
del ListOfData[date]
date = '2004 Feb'
del ListOfData[date]
date = '2004 Mar'
del ListOfData[date]
date = '2004 Apr'
del ListOfData[date]
date = '2004 May'
del ListOfData[date]
date = '2004 Jun'
del ListOfData[date]
date = '2004 Jul'
del ListOfData[date]
date = '2004 Aug'
del ListOfData[date]
date = '2004 Sep'
del ListOfData[date]
date = '2004 Oct'
del ListOfData[date]
date = '2004 Nov'
del ListOfData[date]
date = '2004 Dec'
del ListOfData[date]

date = '2005 Jan'
del ListOfData[date]
date = '2005 Feb'
del ListOfData[date]
date = '2005 Mar'
del ListOfData[date]
date = '2005 Apr'
del ListOfData[date]
date = '2005 May'
del ListOfData[date]
date = '2005 Jun'
del ListOfData[date]
date = '2005 Jul'
del ListOfData[date]
date = '2005 Aug'
del ListOfData[date]
date = '2005 Sep'
del ListOfData[date]
date = '2005 Oct'
del ListOfData[date]
date = '2005 Nov'
del ListOfData[date]
date = '2005 Dec'
del ListOfData[date]

date = '2006 Jan'
del ListOfData[date]
date = '2006 Feb'
del ListOfData[date]
date = '2006 Mar'
del ListOfData[date]
date = '2006 Apr'
del ListOfData[date]
date = '2006 May'
del ListOfData[date]
date = '2006 Jun'
del ListOfData[date]
date = '2006 Jul'
del ListOfData[date]
date = '2006 Aug'
del ListOfData[date]
date = '2006 Sep'
del ListOfData[date]
date = '2006 Oct'
del ListOfData[date]
date = '2006 Nov'
del ListOfData[date]
date = '2006 Dec'
del ListOfData[date]

date = '2007 Jan'
del ListOfData[date]
date = '2007 Feb'
del ListOfData[date]
date = '2007 Mar'
del ListOfData[date]
date = '2007 Apr'
del ListOfData[date]
date = '2007 May'
del ListOfData[date]
date = '2007 Jun'
del ListOfData[date]
date = '2007 Jul'
del ListOfData[date]
date = '2007 Aug'
del ListOfData[date]
date = '2007 Sep'
del ListOfData[date]
date = '2007 Oct'
del ListOfData[date]
date = '2007 Nov'
del ListOfData[date]
date = '2007 Dec'
del ListOfData[date]

date = '2008 Jan'
del ListOfData[date]
date = '2008 Feb'
del ListOfData[date]
date = '2008 Mar'
del ListOfData[date]
date = '2008 Apr'
del ListOfData[date]
date = '2008 May'
del ListOfData[date]
date = '2008 Jun'
del ListOfData[date]
date = '2008 Jul'
del ListOfData[date]
date = '2008 Aug'
del ListOfData[date]
date = '2008 Sep'
del ListOfData[date]
date = '2008 Oct'
del ListOfData[date]
date = '2008 Nov'
del ListOfData[date]
date = '2008 Dec'
del ListOfData[date]

date = '2009 Jan'
del ListOfData[date]
date = '2009 Feb'
del ListOfData[date]
date = '2009 Mar'
del ListOfData[date]
date = '2009 Apr'
del ListOfData[date]
date = '2009 May'
del ListOfData[date]
date = '2009 Jun'
del ListOfData[date]
date = '2009 Jul'
del ListOfData[date]
date = '2009 Aug'
del ListOfData[date]
date = '2009 Sep'
del ListOfData[date]
date = '2009 Oct'
del ListOfData[date]
date = '2009 Nov'
del ListOfData[date]
date = '2009 Dec'
del ListOfData[date]

date = '2010 Jan'
del ListOfData[date]
date = '2010 Feb'
del ListOfData[date]
date = '2010 Mar'
del ListOfData[date]
date = '2010 Apr'
del ListOfData[date]
date = '2010 May'
del ListOfData[date]
date = '2010 Jun'
del ListOfData[date]
date = '2010 Jul'
del ListOfData[date]
date = '2010 Aug'
del ListOfData[date]
date = '2010 Sep'
del ListOfData[date]
date = '2010 Oct'
del ListOfData[date]
date = '2010 Nov'
del ListOfData[date]
date = '2010 Dec'
del ListOfData[date]

date = '2011 Jan'
del ListOfData[date]
date = '2011 Feb'
del ListOfData[date]
date = '2011 Mar'
del ListOfData[date]
date = '2011 Apr'
del ListOfData[date]
date = '2011 May'
del ListOfData[date]
date = '2011 Jun'
del ListOfData[date]
date = '2011 Jul'
del ListOfData[date]
date = '2011 Aug'
del ListOfData[date]
date = '2011 Sep'
del ListOfData[date]
date = '2011 Oct'
del ListOfData[date]
date = '2011 Nov'
del ListOfData[date]
date = '2011 Dec'
del ListOfData[date]

date = '2012 Jan'
del ListOfData[date]
date = '2012 Feb'
del ListOfData[date]
date = '2012 Mar'
del ListOfData[date]
date = '2012 Apr'
del ListOfData[date]
date = '2012 May'
del ListOfData[date]
date = '2012 Jun'
del ListOfData[date]
date = '2012 Jul'
del ListOfData[date]
date = '2012 Aug'
del ListOfData[date]
date = '2012 Sep'
del ListOfData[date]
date = '2012 Oct'
del ListOfData[date]
date = '2012 Nov'
del ListOfData[date]
date = '2012 Dec'
del ListOfData[date]

date = '2013 Jan'
del ListOfData[date]
date = '2013 Feb'
del ListOfData[date]
date = '2013 Mar'
del ListOfData[date]
date = '2013 Apr'
del ListOfData[date]
date = '2013 May'
del ListOfData[date]
date = '2013 Jun'
del ListOfData[date]
date = '2013 Jul'
del ListOfData[date]
date = '2013 Aug'
del ListOfData[date]
date = '2013 Sep'
del ListOfData[date]
date = '2013 Oct'
del ListOfData[date]
date = '2013 Nov'
del ListOfData[date]
date = '2013 Dec'
del ListOfData[date]

date = '2014 Jan'
del ListOfData[date]
date = '2014 Feb'
del ListOfData[date]
date = '2014 Mar'
del ListOfData[date]
date = '2014 Apr'
del ListOfData[date]
date = '2014 May'
del ListOfData[date]
date = '2014 Jun'
del ListOfData[date]
date = '2014 Jul'
del ListOfData[date]
date = '2014 Aug'
del ListOfData[date]
date = '2014 Sep'
del ListOfData[date]
date = '2014 Oct'
del ListOfData[date]
date = '2014 Nov'
del ListOfData[date]
date = '2014 Dec'
del ListOfData[date]

date = '2015 Jan'
del ListOfData[date]
date = '2015 Feb'
del ListOfData[date]
date = '2015 Mar'
del ListOfData[date]
date = '2015 Apr'
del ListOfData[date]
date = '2015 May'
del ListOfData[date]
date = '2015 Jun'
del ListOfData[date]
date = '2015 Jul'
del ListOfData[date]
date = '2015 Aug'
del ListOfData[date]
date = '2015 Sep'
del ListOfData[date]
date = '2015 Oct'
del ListOfData[date]
date = '2015 Nov'
del ListOfData[date]
date = '2015 Dec'
del ListOfData[date]

date = '2016 Jan'
del ListOfData[date]
date = '2016 Feb'
del ListOfData[date]
date = '2016 Mar'
del ListOfData[date]
date = '2016 Apr'
del ListOfData[date]
date = '2016 May'
del ListOfData[date]
date = '2016 Jun'
del ListOfData[date]
date = '2016 Jul'
del ListOfData[date]
date = '2016 Aug'
del ListOfData[date]
date = '2016 Sep'
del ListOfData[date]
date = '2016 Oct'
del ListOfData[date]
date = '2016 Nov'
del ListOfData[date]
date = '2016 Dec'
del ListOfData[date]

date = '2017 Jan'
del ListOfData[date]
date = '2017 Feb'
del ListOfData[date]
date = '2017 Mar'
del ListOfData[date]
date = '2017 Apr'
del ListOfData[date]
date = '2017 May'
del ListOfData[date]
date = '2017 Jun'
del ListOfData[date]
date = '2017 Jul'
del ListOfData[date]
date = '2017 Aug'
del ListOfData[date]
date = '2017 Sep'
del ListOfData[date]
date = '2017 Oct'
del ListOfData[date]
date = '2017 Nov'
del ListOfData[date]
date = '2017 Dec'
del ListOfData[date]

date = '2018 Jan'
del ListOfData[date]
date = '2018 Feb'
del ListOfData[date]
date = '2018 Mar'
del ListOfData[date]
date = '2018 Apr'
del ListOfData[date]
date = '2018 May'
del ListOfData[date]
date = '2018 Jun'
del ListOfData[date]
date = '2018 Jul'
del ListOfData[date]
date = '2018 Aug'
del ListOfData[date]
date = '2018 Sep'
del ListOfData[date]
date = '2018 Oct'
del ListOfData[date]
date = '2018 Nov'
del ListOfData[date]
date = '2018 Dec'
del ListOfData[date]

date = '2019 Jan'
del ListOfData[date]
date = '2019 Feb'
del ListOfData[date]
date = '2019 Mar'
del ListOfData[date]
date = '2019 Apr'
del ListOfData[date]
date = '2019 May'
del ListOfData[date]
date = '2019 Jun'
del ListOfData[date]
date = '2019 Jul'
del ListOfData[date]
date = '2019 Aug'
del ListOfData[date]
date = '2019 Sep'
del ListOfData[date]
date = '2019 Oct'
del ListOfData[date]
date = '2019 Nov'
del ListOfData[date]
date = '2019 Dec'
del ListOfData[date]

date = '2020 Jan'
del ListOfData[date]
date = '2020 Feb'
del ListOfData[date]
date = '2020 Mar'
del ListOfData[date]
date = '2020 Apr'
del ListOfData[date]
date = '2020 May'
del ListOfData[date]
date = '2020 Jun'
del ListOfData[date]



# ListOfData = ListOfData['1979 Dec'].str.split(' ', n=1, expand=True)
# ListOfData = ListOfData[ListOfData.Variables == 'Southeast Asia']

print(ListOfData)
