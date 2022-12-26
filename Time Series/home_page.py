import streamlit as st

#title
def title():
    st.markdown(
        f"""<h1>Buying And Selling Currency Pairs</h1>""",unsafe_allow_html=True
    )

def add_bg_from_url(URL):
    st.markdown(
         f"""
         <style>
         .stApp {URL}
         </style>
         """,
         unsafe_allow_html=True
     )


# General information
def gi():
    st.markdown(f"<p style='font-size:25px'>What is trading?</p>",unsafe_allow_html=True)

    st.markdown(f'<p>Forex trading is the <em>simultaneous</em> buying of one currency and selling of another.</p>',unsafe_allow_html=True)

    st.markdown(f"<p>Currencies are traded through a <a href='https://www.babypips.com/learn/forex/how-to-choose-forex-broker' target='_blank' rel='noopener noopener'>forex broker</a>” or “CFD provider” and are <strong>traded in pairs</strong>.&nbsp;Currencies are quoted in relation to <em>another</em> currency.</p><p>For example, the euro and the U.S. dollar (<strong>EUR/USD</strong>) or the British pound and the Japanese yen (<strong>GBP/JPY</strong>).</p><p><strong></strong></p>",unsafe_allow_html=True)

    st.markdown(f"""
    <strong>When you trade in the forex market, you buy or sell in currency pairs.</strong>
<p><img loading="lazy" class="aligncenter lazyload" title="Buying and Selling in Currency Pairs" src="https://bpcdn.co/images/2016/05/pre-school-tug-of-war.png" alt="Buying and Selling in Currency Pairs" width="490" height="166" border="0"></p>

<p>Imagine each <a href="https://www.babypips.com/forexpedia/currency-pair" target="_blank" rel="noopener noopener">currency pair</a> constantly in a “tug of war” with each currency on its own side of the rope.</p>

<p>An exchange rate is the relative price of two currencies from two different countries.</p>

<p>Exchange rates fluctuate based on <a href="https://marketmilk.babypips.com/currency-strength" target="_blank" rel="noopener noopener">which currency is stronger</a> at the moment.</p>
<p>There are three categories of currency pairs:</p>

<ol>
<li>The “<strong>majors</strong>“</li>
<li>The “<strong>crosses</strong>“</li>
<li>The “<strong>exotics</strong>“</li>
</ol>

<p>The major currency pairs <em>always</em> include the U.S. dollar.</p>

<p>Cross-currency pairs do NOT include the U.S. dollar. Crosses that involve any of the major currencies are also known as ” minors”.</p>

<p>Exotic currency pairs consist of one major currency and one currency from an emerging market (EM).</p>

<h2>Major Currency Pairs</h2>
<p><img loading="lazy" class="size-full wp-image-106947 aligncenter lazyload" src="https://bpcdn.co/images/2011/04/eur-usd.png" alt="EUR/USD Currency Pair" width="582" height="401" sizes="(max-width: 582px) 100vw, 582px" srcset="https://bpcdn.co/images/2011/04/eur-usd.png 582w, https://bpcdn.co/images/2011/04/eur-usd-360x248.png 360w"></p>

<p>The currency pairs listed below are considered the “<strong>majors.</strong>”</p>

<p>These pairs all contain the U.S. dollar (<strong>USD</strong>) on one side and are the most frequently traded.</p>

<p>While there are EIGHT major <em>currencies</em>, there are only SEVEN major <em>currency pairs</em>.</p>

<p>Compared to the crosses and exotics, the price moves more frequently with the majors, which provides more trading opportunities.</p>
<div>
<p>The majors are the most <strong>liquid</strong>&nbsp;in the world.</p>
<p><a href="https://www.babypips.com/forexpedia/liquidity" target="_blank" rel="noopener noopener">Liquidity</a> is used to describe the level of activity in the financial market.</p>
</div>
<div>In forex, it’s based on the number of active traders buying and selling a specific currency pair and the 
<a href="https://www.babypips.com/forexpedia/volume" target="_blank" rel="noopener noopener">volume</a>
    being traded.
<p>The more frequently traded something is the higher its liquidity.</p>

<p>This means that EUR/USD is more liquid than AUD/USD.</p>
<h2>Major Cross-Currency Pairs or Minor Currency Pairs</h2>
<p>Currency pairs that include any two of the major currencies <em>except</em> the U.S. dollar are known as <strong>cross-currency pairs</strong> or simply as the “<strong>crosses</strong>.”</p>
<p>Major crosses are also known as “<strong>minors</strong>.”</p>
<p>While not as frequently traded as the majors, the crosses are still pretty liquid and still provide plenty of trading opportunities.</p>
<p>The most actively traded crosses are derived from the three major non-USD currencies: </p><strong>EUR; </strong><strong>JPY; </strong><strong>and GBP</strong>

<h3>Euro Crosses</h3>

<table class="ScrollableTable-module__table___neLIx ScrollableTable-module__scrollable___qWhmW" border="0" width="525">
<tbody>
<tr>
<th>Currency Pair</th>
<th>Countries</th>
<th><strong>FX Geek Speak</strong></th>
</tr>
<tr>
<td align="center" width="90"><a href="https://marketmilk.babypips.com/symbols/EURCHF/overview" target="_blank" rel="noopener noopener">EUR/CHF</a></td>
<td align="center">Eurozone / Switzerland</td>
<td align="center">“euro swissy”</td>
</tr>
<tr>
<td align="center" width="90"><a href="https://marketmilk.babypips.com/symbols/EURGBP/overview" target="_blank" rel="noopener noopener">EUR/GBP</a></td>
<td align="center">Eurozone / United Kingdom</td>
<td align="center">“euro pound”</td>
</tr>
<tr>
<td align="center" width="90"><a href="https://marketmilk.babypips.com/symbols/EURCAD/overview" target="_blank" rel="noopener noopener">EUR/CAD</a></td>
<td align="center">Eurozone / Canada</td>
<td align="center">“euro loonie”</td>
</tr>
<tr>
<td align="center" width="90"><a href="https://marketmilk.babypips.com/symbols/EURAUD/overview" target="_blank" rel="noopener noopener">EUR/AUD</a></td>
<td align="center">Eurozone / Australia</td>
<td align="center">“euro aussie”</td>
</tr>
<tr>
<td align="center" width="90"><a href="https://marketmilk.babypips.com/symbols/EURNZD/overview" target="_blank" rel="noopener noopener">EUR/NZD</a></td>
<td align="center">Eurozone / New Zealand</td>
<td align="center">“euro kiwi”</td>
</tr>
<tr>
<td align="center" width="90"><a href="https://marketmilk.babypips.com/symbols/EURSEK/overview" target="_blank" rel="noopener noopener">EUR/SEK</a></td>
<td align="center">Eurozone / Sweden</td>
<td align="center">“euro stockie”</td>
</tr>
<tr>
<td align="center" width="90"><a href="https://marketmilk.babypips.com/symbols/EURNOK/overview" target="_blank" rel="noopener noopener">EUR/NOK</a></td>
<td align="center">Eurozone / Norway</td>
<td align="center">“euro nockie”</td>
</tr>
</tbody>
</table>

<h2>Exotic Currency Pairs</h2>
<p>No, exotic pairs are not exotic belly dancers who happen to be twins.</p>
<p>An <strong>exotic currency</strong> is a currency from countries with&nbsp;developing or emerging markets.</p>
<p><strong>Exotic currency pairs</strong> are made up of one major currency paired with the currency of an emerging economy, such as Brazil, Mexico, Chile, Turkey, or Hungary.</p>
<p>Basically, an exotic currency pair includes&nbsp;<b>one major currency alongside an exotic currency.&nbsp;</b></p>
<p>The chart below contains a few examples of exotic currency pairs.</p>

<p>Wanna take a shot at guessing what those other currency symbols stand for?</p>
<p>Depending on your forex broker, you may see the following exotic currency pairs so it’s good to know what they are.</p>
<p>Keep in mind that these pairs aren’t as heavily traded as the “majors” or “crosses,” so the transaction costs associated with trading these pairs are usually bigger.</p>
<p>It’s not unusual to see spreads that are two or three times bigger than that of EUR/USD or USD/JPY.</p>
<p>Due to the overall lower degree of liquidity, exotic currency pairs tend to be far more sensitive to economic and geopolitical events.</p>
<p>For example, a political scandal or unexpected election results can cause an exotic pair’s exchange rate to swing violently.</p>
<p>So if you want to trade exotics currency pairs, remember to factor this into your decision.</p>
<p>For those of y’all who are really mesmerized by exotics, here’s a more comprehensive list.</p>
<div><div class="ScrollableTable-module__container___hfbgx"><div class="ScrollableTable-module__overlay___LciK8" style="top: 0px;"></div><table class="ScrollableTable-module__table___neLIx ScrollableTable-module__scrollable___qWhmW">
<tbody>
<tr>
<th>Currency Code</th>
<th>Country</th>
<th>Currency Code</th>
<th>Country</th>
</tr>
<tr>
<td>AED</td>
<td>UAE Dirham</td>
<td>ARS</td>
<td>Argentinean Peso</td>
</tr>
<tr>
<td>AFN</td>
<td>Afghanistan Afghani</td>
<td>GEL</td>
<td>Georgian Lari</td>
</tr>
<tr>
<td>MYR</td>
<td>Malaysian Ringgit</td>
<td>AMD</td>
<td>Armenian Dram</td>
</tr>
<tr>
<td>GYD</td>
<td>Guyanese Dollar</td>
<td>MZN</td>
<td>Mozambique new Metical</td>
</tr>
<tr>
<td>AWG</td>
<td>Aruban Florin</td>
<td>IDR</td>
<td>Indonesian Rupiah</td>
</tr>
<tr>
<td>OMR</td>
<td>Omani Rial</td>
<td>AZN</td>
<td>Azerbaijan New Manat</td>
</tr>
<tr>
<td>IQD</td>
<td>Iraqi Dinar</td>
<td>QAR</td>
<td>Qatari Rial</td>
</tr>
<tr>
<td>BHD</td>
<td>Bahraini Dinar</td>
<td>IRR</td>
<td>Iranian Rial</td>
</tr>
<tr>
<td>SLL</td>
<td>Sierra Leone Leone</td>
<td>BWP</td>
<td>Botswana Pula</td>
</tr>
<tr>
<td>JOD</td>
<td>Jordanian Dinar</td>
<td>TJS</td>
<td>Tajikistani Somoni</td>
</tr>
<tr>
<td>BYR</td>
<td>Belarusian Ruble</td>
<td>KGS</td>
<td>Kyrgyzstani Som</td>
</tr>
<tr>
<td>TMT</td>
<td>Turkmenistan new Manat</td>
<td>CDF</td>
<td>Congolese Franc</td>
</tr>
<tr>
<td>LBP</td>
<td>Lebanese Pound</td>
<td>TZS</td>
<td>Tanzanian Schilling</td>
</tr>
<tr>
<td>DZD</td>
<td>Algerian Dinar</td>
<td>LRD</td>
<td>Liberian Dollar</td>
</tr>
<tr>
<td>UZS</td>
<td>Uzbekistan Som</td>
<td>EGP</td>
<td>Egyptian Pound</td>
</tr>
<tr>
<td>MAD</td>
<td>Moroccan Dirham</td>
<td>WST</td>
<td>Samoan Tala</td>
</tr>
<tr>
<td>EEK</td>
<td>Estonian Kroon</td>
<td>MNT</td>
<td>Mongolian Tugrik</td>
</tr>
<tr>
<td>MWK</td>
<td>Malawi Kwacha</td>
<td>ETB</td>
<td>Ethiopian Birr</td>
</tr>
<tr>
<td>THB</td>
<td>Thai Baht</td>
<td>TRY</td>
<td>New Turkish Lira</td>
</tr>
<tr>
<td>ZAR</td>
<td>South African Rand</td>
<td>ZWD</td>
<td>Zimbabwe Dollar</td>
</tr>
<tr>
<td>BRL</td>
<td>Brazilian Real</td>
<td>CLP</td>
<td>Chilean Peso</td>
</tr>
<tr>
<td>CNY</td>
<td>Chinese Yuan Renminbi</td>
<td>CZK</td>
<td>Czech Koruna</td>
</tr>
<tr>
<td>HKD</td>
<td>Hong Kong Dollar</td>
<td>HUF</td>
<td>Hungarian Forint</td>
</tr>
<tr>
<td>ILS</td>
<td>Israeli Shekel</td>
<td>INR</td>
<td>Indian Rupee</td>
</tr>
<tr>
<td>ISK</td>
<td>Icelandic Krona</td>
<td>KRW</td>
<td>South Korean Won</td>
</tr>
<tr>
<td>KWD</td>
<td>Kuwaiti Dinar</td>
<td>MXN</td>
<td>Mexican Peso</td>
</tr>
<tr>
<td>PHP</td>
<td>Philippine Peso</td>
<td>PKR</td>
<td>Pakistani Rupee</td>
</tr>
<tr>
<td>PLN</td>
<td>Polish Zloty</td>
<td>RUB</td>
<td>Russian Ruble</td>
</tr>
<tr>
<td>SAR</td>
<td>Saudi Arabian Riyal</td>
<td>SGD</td>
<td>Singaporean Dollar</td>
</tr>
<tr>
<td>TWD</td>
<td>Taiwanese Dollar</td>
<td></td>
<td></td>
</tr>
</tbody>
</table></div></div>
<p>Aside from the three main categories of currency pairs, there are other “groups” of currencies that are thrown around in the FX world that you should be aware of.</p>
<h2>G10 Currencies</h2>
<p>The G10 currencies are ten of the most heavily traded currencies in the world, which are also ten of the world’s most liquid currencies.</p>

<p>Traders regularly buy and sell them in an open market with minimal impact on their own international exchange rates.</p>
<div><div class="ScrollableTable-module__container___hfbgx"><div class="ScrollableTable-module__overlay___LciK8" style="top: 0px;"></div><table class="ScrollableTable-module__table___neLIx ScrollableTable-module__scrollable___qWhmW" border="0" width="525">
<tbody>
<tr>
<th style="text-align: center;">Country</th>
<th style="text-align: center;">Currency Name</th>
<th style="text-align: center;">Currency Code</th>
</tr>
<tr>
<td style="text-align: center;" align="center" width="90">United States</td>
<td style="text-align: center;" align="center">dollar</td>
<td style="text-align: center;" align="center">USD</td>
</tr>
<tr>
<td style="text-align: center;" align="center" width="90">European Union</td>
<td style="text-align: center;" align="center">euro</td>
<td style="text-align: center;" align="center">EUR</td>
</tr>
<tr>
<td style="text-align: center;" align="center" width="90">United Kingdom</td>
<td style="text-align: center;" align="center">pound</td>
<td style="text-align: center;" align="center">GBP</td>
</tr>
<tr>
<td style="text-align: center;" align="center" width="90">Japan</td>
<td style="text-align: center;" align="center">yen</td>
<td style="text-align: center;" align="center">JPY</td>
</tr>
<tr>
<td style="text-align: center;" align="center" width="90">Australia</td>
<td style="text-align: center;" align="center">dollar</td>
<td style="text-align: center;" align="center">AUD</td>
</tr>
<tr>
<td style="text-align: center;" align="center" width="90">New Zealand</td>
<td style="text-align: center;" align="center">dollar</td>
<td style="text-align: center;" align="center">NZD</td>
</tr>
<tr>
<td style="text-align: center;" align="center" width="90">Canada</td>
<td style="text-align: center;" align="center">dollar</td>
<td style="text-align: center;" align="center">CAD</td>
</tr>
<tr>
<td style="text-align: center;" align="center" width="90">Switzerland</td>
<td style="text-align: center;" align="center">franc</td>
<td style="text-align: center;" align="center">CHF</td>
</tr>
<tr>
<td style="text-align: center;" align="center" width="90">Norway</td>
<td style="text-align: center;" align="center">krone</td>
<td style="text-align: center;" align="center">NOK</td>
</tr>
<tr>
<td style="text-align: center;" align="center" width="90">Sweden</td>
<td style="text-align: center;" align="center">krona</td>
<td style="text-align: center;" align="center">SEK</td>
</tr>
<tr>
<td style="text-align: center;" align="center" width="90">Denmark</td>
<td style="text-align: center;" align="center">krone</td>
<td style="text-align: center;" align="center">DKK</td>
</tr>
</tbody>
</table></div></div>

<h2><strong>The Scandies</strong></h2>
<p>Scandinavia is a subregion in Northern Europe, with strong historical, cultural, and linguistic ties.</p>
<p>The term “<strong>Scandinavia</strong>” in local usage covers the three kingdoms of <strong>Denmark, Norway, and Sweden.</strong></p>
<p>Together, their currencies are known as the “</p>
<strong>Scandies</strong>
<p>.</p>
<p>Back in the day, Denmark and Sweden established the <a href="https://en.wikipedia.org/wiki/Scandinavian_Monetary_Union" target="_blank" rel="noopener noopener">Scandinavian Monetary Union</a> to merge their currencies to a gold standard. Norway joined later.</p>
<p>This meant that these countries now had one currency, with the same monetary value, with the exception that each of these countries minted its own coins.</p>

<p>But then World War I happened, the gold standard was abandoned and the Scandinavian Monetary Union disbanded.&nbsp; These countries decided to keep the currency, even if the values were separate from one another. And this remains the state of things.</p>

<p>If you notice their currency names, they all look similar. That’s because the word “krone or krona” literally means “crown”, and the differences in spelling of the name represent the differences between the North Germanic languages.</p>
<p>Crown currencies. What a cool name huh?</p>
<p>I don’t know about you, but saying “Hook me up with some crowns yo.” sounds way cooler than “Hook me up with some dollahs yo.”</p>
<div><div class="ScrollableTable-module__container___hfbgx"><div class="ScrollableTable-module__overlay___LciK8" style="top: 0px;"></div><table class="ScrollableTable-module__table___neLIx ScrollableTable-module__scrollable___qWhmW" border="0" width="525">
<tbody>
<tr>
<th style="text-align: center;">Country</th>
<th style="text-align: center;">Currency Name</th>
<th style="text-align: center;">Currency Code</th>
</tr>
<tr>
<td style="text-align: center;" align="center" width="90">Denmark</td>
<td style="text-align: center;" align="center">krone</td>
<td style="text-align: center;" align="center">DKK</td>
</tr>
<tr>
<td style="text-align: center;" align="center" width="90">Sweden</td>
<td style="text-align: center;" align="center">krona</td>
<td style="text-align: center;" align="center">SEK</td>
</tr>
<tr>
<td style="text-align: center;" align="center" width="90">Norway</td>
<td style="text-align: center;" align="center">krone</td>
<td style="text-align: center;" align="center">NOK</td>
</tr>
</tbody>
</table></div></div>
    <p>SEK and NOK also have cool nicknames, “<strong>Stockie</strong>” and “<strong>Nokie</strong>“.</p>
    <p>So when paired with the U.S. dollar,&nbsp; USD/SEK is read “dollar stockie”&nbsp; and USD/NOK is read “dollar nockie”.</p>
    <h2><strong>CEE Currencies</strong></h2>
    <p>“<strong>CEE</strong>” stands for <strong>Central and Eastern Europe</strong>.</p>
    <p>Central and Eastern Europe is a term encompassing the countries in <strong>Central Europe,&nbsp;</strong>&nbsp;the <strong>Baltics</strong>,<strong> Eastern Europe</strong>, and <strong>Southeast Europe</strong> (the Balkans), usually meaning former communist states from the <strong>Eastern Bloc</strong> (Warsaw Pact) in Europe.</p>
    <p><strong></strong></p>
    <strong>Central and Eastern European Countries (CEECs)</strong>.
     is an OECD term for the group of countries comprising Albania, Bulgaria, Croatia, the Czech Republic, Hungary, Poland, Romania, the Slovak Republic, Slovenia, and the three Baltic States: Estonia, Latvia, and Lithuania.
    <p></p>
    <p>Regarding the FX market, there are four main CEE currencies to be aware of.</p>
    <p>Whew! That was a lot of information on currencies but you just raised your FX IQ points!&nbsp;🧠</p>

<p>Let’s summarize what you’ve learned in a series of questions:</p>
<p><strong>What is a currency pair in forex?</strong><br>
A currency pair is a pairing of currencies where the value of one is relative to the other. For example, GBP/USD is the value of the British pound relative to the U.S. dollar.</p>
<p><strong>What are the major currency pairs?</strong><br>
Major currency pairs (“majors”) are those that include the U.S. dollar and are the most frequently traded. There are seven of them: EUR/USD, USD/JPY, GBP/USD, USD/CAD, USD/CHF, AUD/USD, and NZD/USD.</p>
<p><strong>What are the currency crosses?</strong><br>
Currency crosses (“crosses”) are the more frequently traded currencies that do NOT include the U.S. dollar in their pairing. Crosses include EUR/GBP, EUR/CAD, GBP/JPY, EUR/CHF, EUR/JPY, etc.</p>
<p><strong>How many currency pairs exist?</strong><br>
There are HUNDREDS of currency pairs in existence but not all can be traded in the FX market. The United Nations currently recognizes 180 currencies. If you were to pair each currency up with another, it’s a lot.</p>
    """
    ,unsafe_allow_html=True)



# https://www.babypips.com/learn/forex/buying-selling-currency-pairs
# add_bg_from_url() 

def header(url):
     st.markdown(f'<p style="background-color:#f2f3f4;color:#4b5320;font-size:24px;border-radius:2%;text-align:center">{url}</p>', unsafe_allow_html=True)

# header("Forecasting")

def header(url):
     st.write(f'<p style="color:#4b5320;font-size:24px;text-align:center">{url}</p>', unsafe_allow_html=True)


# header('Navigate to relevant Page')

def content(url):
     st.write(f'<p style="color:#4b5320;font-size:24px;text-align:center">{url}</p>', unsafe_allow_html=True)
