import urllib, json, sys
import spreadsheet

def read_json(stockName):

    # url string
    url = "http://www.isaham.my/api/stock/"+stockName
    
    # load url data
    try:
        response = urllib.urlopen(url)
        return json.loads(response.read())
    except:
        print "Error invalid stock name"
        sys.exit(1)

# Formatting the fundemental ratio
def fundamental_ratio_calc (stock):
    #Spreadsheet API
    variableFullName = spreadsheet.fetchSpreadSheet()
    
    f_ratioArray = []

    #PE ratio
    if stock['pe'] < stock['avg_pe']-1:
        data = {'name': variableFullName['pe'], 'color': 'green', 'val': stock['pe']}
        f_ratioArray.append(data)
    elif stock['pe'] > stock['avg_pe']+1:
        data = {'name': variableFullName['pe'], 'color': 'red', 'val': stock['pe']}
        f_ratioArray.append(data)
    else:
        data = {'name': variableFullName['pe'], 'color': 'black', 'val': stock['pe']}
        f_ratioArray.append(data)

    # EV / EBITDA
    if stock['ev_ebitda'] < stock['avg_ev_ebitda']-1:
        data = {'name': variableFullName['ev_ebitda'], 'color': 'green', 'val': stock['ev_ebitda']}
        f_ratioArray.append(data)
    elif stock['ev_ebitda'] > stock['avg_ev_ebitda']+1:
        data = {'name': variableFullName['ev_ebitda'], 'color': 'red', 'val': stock['ev_ebitda']}
        f_ratioArray.append(data)
    else:
        data = {'name': variableFullName['ev_ebitda'], 'color': 'black', 'val': stock['ev_ebitda']}
        f_ratioArray.append(data)

    # PEG
    if 0 < stock['peg'] < 1.0:
        data = {'name': variableFullName['peg'], 'color': 'green', 'val': stock['peg']}
        f_ratioArray.append(data)
    elif stock['peg'] > 1.5 or stock['peg'] <= 0:
        data = {'name': variableFullName['peg'], 'color': 'red', 'val': stock['peg']}
        f_ratioArray.append(data)
    else:
        data = {'name': variableFullName['peg'], 'color': 'black', 'val': stock['peg']}
        f_ratioArray.append(data)

    # Sharpe Ratio (3 yrs)
    if stock['sharpe_ratio_600'] > 0.5:
        data = {'name': variableFullName['sharpe_ratio_600'], 'color': 'green', 'val': stock['sharpe_ratio_600']}
        f_ratioArray.append(data) 
    elif stock['sharpe_ratio_600'] < 0.0:
        data = {'name': variableFullName['sharpe_ratio_600'], 'color': 'red', 'val': stock['sharpe_ratio_600']}
        f_ratioArray.append(data)
    else:
        data = {'name': variableFullName['sharpe_ratio_600'], 'color': 'black', 'val': stock['sharpe_ratio_600']}
        f_ratioArray.append(data)

    # LTS Score
    if stock['lts_score'] > 7.5:
        data = {'name': variableFullName['lts_score'], 'color': 'green', 'val': stock['lts_score']}
        f_ratioArray.append(data)
    elif stock['lts_score'] < 4.0:
        data = {'name': variableFullName['lts_score'], 'color': 'red', 'val': stock['lts_score']}
        f_ratioArray.append(data)
    else:
        data = {'name': variableFullName['lts_score'], 'color': 'black', 'val': stock['lts_score']}
        f_ratioArray.append(data)

    # Altman Z
    if stock['z'] > 3:
        data = {'name': variableFullName['z'], 'color': 'green', 'val': stock['z']}
        f_ratioArray.append(data)
    elif stock['z'] < 1.8:
        data = {'name': variableFullName['z'], 'color': 'red', 'val': stock['z']}
        f_ratioArray.append(data)
    else:
        data = {'name': variableFullName['z'], 'color': 'black', 'val': stock['z']}
        f_ratioArray.append(data)
    
    # Beaver
    if stock['beaver'] > 0.06:
        data = {'name': variableFullName['beaver'], 'color': 'green', 'val': stock['beaver']}
        f_ratioArray.append(data)
    elif stock['beaver'] < 0.03:
        data = {'name': variableFullName['beaver'], 'color': 'red', 'val': stock['beaver']}
        f_ratioArray.append(data)
    else:
        data = {'name': variableFullName['beaver'], 'color': 'black', 'val': stock['beaver']}
        f_ratioArray.append(data)

    # Current Ratio
    if stock['current_ratio'] > 2:
        data = {'name': variableFullName['current_ratio'], 'color': 'green', 'val': stock['current_ratio']}
        f_ratioArray.append(data)
    elif stock['current_ratio'] < 1.5:
        data = {'name': variableFullName['current_ratio'], 'color': 'red', 'val': stock['current_ratio']}
        f_ratioArray.append(data)
    else:
        data = {'name': variableFullName['current_ratio'], 'color': 'black', 'val': stock['current_ratio']}
        f_ratioArray.append(data)

    # Debt / Equity (DE) Ratio
    if stock['de'] < 0.5:
        data = {'name': variableFullName['de'], 'color': 'green', 'val': stock['de']}
        f_ratioArray.append(data)
    elif stock['de'] > 1.0:
        data = {'name': variableFullName['de'], 'color': 'red', 'val': stock['de']}
        f_ratioArray.append(data)
    else:
        data = {'name': variableFullName['de'], 'color': 'black', 'val': stock['de']}
        f_ratioArray.append(data)

    # Revenue QoQ
    if stock['revenue_qoq'] > 5:
        data = {'name': variableFullName['revenue_qoq'], 'color': 'green', 'val': stock['revenue_qoq']}
        f_ratioArray.append(data)
    elif stock['revenue_qoq'] < 0:
        data = {'name': variableFullName['revenue_qoq'], 'color': 'red', 'val': stock['revenue_qoq']}
        f_ratioArray.append(data)
    else:
        data = {'name': variableFullName['revenue_qoq'], 'color': 'black', 'val': stock['revenue_qoq']}
        f_ratioArray.append(data)

    # Profit QoQ
    if stock['profit_qoq'] > 5 and (stock['opi_qoq']*2.0) > stock['profit_qoq']:
        data = {'name': variableFullName['profit_qoq'], 'color': 'green', 'val': stock['profit_qoq']}
        f_ratioArray.append(data)
    elif stock['profit_qoq'] < 0:
        data = {'name': variableFullName['profit_qoq'], 'color': 'red', 'val': stock['profit_qoq']}
        f_ratioArray.append(data)
    else:
        data = {'name': variableFullName['profit_qoq'], 'color': 'black', 'val': stock['profit_qoq']}
        f_ratioArray.append(data)

    # Profit YoY
    if stock['profit_yoy'] > 5:
        data = {'name': variableFullName['profit_yoy'], 'color': 'green', 'val': stock['profit_yoy']}
        f_ratioArray.append(data)
    elif stock['profit_yoy'] < 0:
        data = {'name': variableFullName['profit_yoy'], 'color': 'red', 'val': stock['profit_yoy']}
        f_ratioArray.append(data)
    else:
        data = {'name': variableFullName['profit_yoy'], 'color': 'black', 'val': stock['profit_yoy']}
        f_ratioArray.append(data)

    # NTA QoQ
    if stock['ntaps_qoq'] > 5:
        data = {'name': variableFullName['ntaps_qoq'], 'color': 'green', 'val': stock['ntaps_qoq']}
        f_ratioArray.append(data)
    elif stock['ntaps_qoq'] < 0:
        data = {'name': variableFullName['ntaps_qoq'], 'color': 'red', 'val': stock['ntaps_qoq']}
        f_ratioArray.append(data)
    else:
        data = {'name': variableFullName['ntaps_qoq'], 'color': 'black', 'val': stock['ntaps_qoq']}
        f_ratioArray.append(data)

    # Profit Margin
    if stock['margin'] > 15:
        data = {'name': variableFullName['margin'], 'color': 'green', 'val': stock['margin']}
        f_ratioArray.append(data)
    elif stock['margin'] < 5:
        data = {'name': variableFullName['margin'], 'color': 'red', 'val': stock['margin']}
        f_ratioArray.append(data)
    else:
        data = {'name': variableFullName['margin'], 'color': 'black', 'val': stock['margin']}
        f_ratioArray.append(data)

    # ROE
    if stock['roe'] > 15:
        data = {'name': variableFullName['roe'], 'color': 'green', 'val': stock['roe']}
        f_ratioArray.append(data)
    elif stock['roe'] < 0.0:
        data = {'name': variableFullName['roe'], 'color': 'red', 'val': stock['roe']}
        f_ratioArray.append(data)
    else:
        data = {'name': variableFullName['roe'], 'color': 'black', 'val': stock['roe']}
        f_ratioArray.append(data)

    # ROIC
    if stock['roic'] > 15:
        data = {'name': variableFullName['roe'], 'color': 'green', 'val': stock['roe']}
        f_ratioArray.append(data)
    elif stock['roic'] < 0.0:
        data = {'name': variableFullName['roe'], 'color': 'red', 'val': stock['roe']}
        f_ratioArray.append(data)
    else:
        data = {'name': variableFullName['roe'], 'color': 'black', 'val': stock['roe']}
        f_ratioArray.append(data)

    # Dividend Per Share (DPS)
    data = {'name': variableFullName['dps'], 'color': 'black', 'val': stock['dps']}
    f_ratioArray.append(data)

    # Dividend Yield (DY)
    if stock['dy'] > 2:
        data = {'name': variableFullName['dy'], 'color': 'green', 'val': stock['dy']}
        f_ratioArray.append(data)
    elif stock['dy'] < 0:
        data = {'name': variableFullName['dy'], 'color': 'red', 'val': stock['dy']}
        f_ratioArray.append(data)
    else:
        data = {'name': variableFullName['dy'], 'color': 'black', 'val': stock['dy']}
        f_ratioArray.append(data)

    # FCF Yield
    if stock['fcf_yield'] > 5:
        data = {'name': variableFullName['fcf_yield'], 'color': 'green', 'val': stock['fcf_yield']}
        f_ratioArray.append(data)
    elif stock['fcf_yield'] < 0:
        data = {'name': variableFullName['fcf_yield'], 'color': 'red', 'val': stock['fcf_yield']}
        f_ratioArray.append(data)
    else:
        data = {'name': variableFullName['fcf_yield'], 'color': 'black', 'val': stock['fcf_yield']}
        f_ratioArray.append(data)
    
    return f_ratioArray

# Formatting Support and Resistance
def supportResistance(stock):
    snrArray = []
    for s in stock['support_vop'][::-1]:
        if s[0] in stock['strong_supports']:
            snrArray.append( {'price': s[0], 'volume': s[1], 'color': '#DAF7A6'} )
        else:
            snrArray.append( {'price': s[0], 'volume': s[1], 'color': '#000'} )
    
    snrArray.append( {'price': stock['lp1'], 'volume': '-', 'color': '#FFF9B2'} )

    for s in stock['resistance_vop']:
        if s[0] in stock['strong_resistances']:
            snrArray.append( {'price': s[0], 'volume': s[1], 'color': '#FFB4B2'} )
        else:
            snrArray.append( {'price': s[0], 'volume': s[1], 'color': '#000'} )
    
    return snrArray

# Formatting Trading Signals
def tradingSignals(stock):

    signalsArray = []

    # MA20
    if stock['lp1'] > stock['ma20']:
        signalsArray.append( {'name': 'Moving Average (Short Term)', 'signal': 'BUY', 'color': '#009900'} )
    elif stock['lp1'] < stock['ma20']:
        signalsArray.append( {'name': 'Moving Average (Short Term)', 'signal': 'SELL', 'color': '#ff1a1a'} )  
    else:
        signalsArray.append( {'name': 'Moving Average (Short Term)', 'signal': 'HOLD', 'color': '#000'} )

    # MA50
    if stock['lp1'] > stock['ma50']:
        signalsArray.append( {'name': 'Moving Average (Mid Term)', 'signal': 'BUY', 'color': '#009900'} )
    elif stock['lp1'] < stock['ma50']:
        signalsArray.append( {'name': 'Moving Average (Mid Term)', 'signal': 'SELL', 'color': '#ff1a1a'} )  
    else:
        signalsArray.append( {'name': 'Moving Average (Mid Term)', 'signal': 'HOLD', 'color': '#000'} )
    
    # MA200
    if stock['lp1'] > stock['ma200']:
        signalsArray.append( {'name': 'Moving Average (Long Term)', 'signal': 'BUY', 'color': '#009900'} )
    elif stock['lp1'] < stock['ma200']:
        signalsArray.append( {'name': 'Moving Average (Long Term)', 'signal': 'SELL', 'color': '#ff1a1a'} )  
    else:
        signalsArray.append( {'name': 'Moving Average (Long Term)', 'signal': 'HOLD', 'color': '#000'} )

    # Ichimoku Kumo
    if 0 <= stock['kumo_cross'] <= 2:
        signalsArray.append( {'name': 'Ichimoku Kumo', 'signal': 'BUY (New)', 'color': '#009900'} )
    elif stock['ichimoku'] == 1:
        signalsArray.append( {'name': 'Ichimoku Kumo', 'signal': 'BUY', 'color': '#009900'} )
    elif stock['ichimoku'] < -1:
        signalsArray.append( {'name': 'Ichimoku Kumo', 'signal': 'SELL', 'color': '#ff1a1a'} )
    else:
        signalsArray.append( {'name': 'Ichimoku Kumo', 'signal': 'HOLD', 'color': '#000'} )

    # Bollinger Band
    if stock['bb_cross'] > 0:
        signalsArray.append( {'name': 'Bollinger Band', 'signal': 'BUY (Oversold Cross)', 'color': '#009900'} )
    elif stock['bb_squeeze_buy'] > 0 and stock['vmar3'] > 0 and stock["no_action"] == 0:
        signalsArray.append( {'name': 'Bollinger Band', 'signal': 'BUY (Squeeze Breakout)', 'color': '#009900'} )
    elif 0 < stock['bb_breakout'] < 6:
        signalsArray.append( {'name': 'Bollinger Band', 'signal': 'BUY (Breakout)', 'color': '#009900'} )
    else:
        signalsArray.append( {'name': 'Bollinger Band', 'signal': '-', 'color': '#000'} )

    # RSI
    if stock['rsi_14'] > 50:
        signalsArray.append( {'name': 'RSI', 'signal': 'BUY', 'color': '#009900'} )
    elif stock['rsi_oversold'] > 0:
        signalsArray.append( {'name': 'RSI', 'signal': 'BUY', 'color': '#009900'} )
    elif stock['rsi_14'] < 50:
        signalsArray.append( {'name': 'RSI', 'signal': 'SELL', 'color': '#ff1a1a'} )
    else:
        signalsArray.append( {'name': 'RSI', 'signal': 'HOLD', 'color': '#000'} )

    # Stochastic
    if stock['sto_14'] > 50:
        signalsArray.append( {'name': 'Stochastic', 'signal': 'BUY', 'color': '#009900'} )
    elif stock['sto_bullish_cross'] > 0:
        signalsArray.append( {'name': 'Stochastic', 'signal': 'BUY', 'color': '#009900'} )
    elif stock['sto_14'] < 50:
        signalsArray.append( {'name': 'Stochastic', 'signal': 'SELL', 'color': '#ff1a1a'} )
    else:
        signalsArray.append( {'name': 'Stochastic', 'signal': 'HOLD', 'color': '#000'} )

    # Heikin-Ashi
    if stock['heikin'] == 1:
        signalsArray.append( {'name': 'Heikin-Ashi', 'signal': 'BUY', 'color': '#009900'} )
    elif stock['ha_bottom'] > 0:
        signalsArray.append( {'name': 'Heikin-Ashi', 'signal': 'BUY', 'color': '#009900'} )
    elif stock['heikin'] == -1:
        signalsArray.append( {'name': 'Heikin-Ashi', 'signal': 'SELL', 'color': '#ff1a1a'} )
    elif stock['ha_top'] > 0:
        signalsArray.append( {'name': 'Heikin-Ashi', 'signal': 'SELL', 'color': '#ff1a1a'} )
    else:
        signalsArray.append( {'name': 'Heikin-Ashi', 'signal': 'HOLD', 'color': '#000'} )

    # MACD
    if stock['macd_4r1g'] == 1 and stock["near_ma20"] == 1 and stock['vma50'] > 500000:
        signalsArray.append( {'name': 'MACD', 'signal': 'BUY (4R1G+MA20)', 'color': '#009900'} )
    elif stock['macd_4r1g'] == 1 and stock["macd_line"] > 0  and stock['vma50'] > 500000:
        signalsArray.append( {'name': 'MACD', 'signal': 'BUY (4R1G+Above 0)', 'color': '#009900'} )
    elif stock['macd_line'] > 0 and stock['macd_cross'] > 0:
        signalsArray.append( {'name': 'MACD', 'signal': 'BUY (New Above 0)', 'color': '#009900'} )
    elif stock['macd_line'] > 0:
        signalsArray.append( {'name': 'MACD', 'signal': 'BUY (Above 0)', 'color': '#009900'} )    
    elif stock['macd_oversold'] > 0:
        signalsArray.append( {'name': 'MACD', 'signal': 'BUY (Oversold Cross)', 'color': '#009900'} )    
    elif stock['macd_line'] < 0:
        signalsArray.append( {'name': 'MACD', 'signal': 'SELL', 'color': '#ff1a1a'} )
    else:    
        signalsArray.append( {'name': 'MACD', 'signal': 'HOLD', 'color': '#000'} )

    # Solid MA Trend
    if stock['solid_ma'] > 0:
        signalsArray.append( {'name': 'Solid MA Trend', 'signal': 'BUY', 'color': '#009900'} )        
    else:
        signalsArray.append( {'name': 'Solid MA Trend', 'signal': '-', 'color': '#000'} )        
    
    # SAT
    if 0.20 <= stock["lp1"] <= 5 and stock["vma50"] > 500000 and stock["ema9_20"] == 1 and stock["rsi_14_upper"] == 1 and stock["macd_line"] > 0 and stock["macd_histogreen"] == 1:
        signalsArray.append( {'name': 'SAT', 'signal': 'BUY', 'color': '#009900'} )                
    elif stock['perf_1w'] < 0.1342329461:
        signalsArray.append( {'name': 'SAT', 'signal': 'SELL', 'color': '#ff1a1a'} )       
    else:
        signalsArray.append( {'name': 'SAT', 'signal': 'HOLD', 'color': '#000'} )

    # Sector Trend (Long Term)
    if stock["avg_trend_lt"] > 0.5:
        signalsArray.append( {'name': 'Sector Trend (Long Term)', 'signal': 'BUY', 'color': '#009900'} )        
    elif stock["avg_trend_lt"] < 0:
        signalsArray.append( {'name': 'Sector Trend (Long Term)', 'signal': 'SELL', 'color': '#ff1a1a'} )
    else:
        signalsArray.append( {'name': 'Sector Trend (Long Term)', 'signal': 'HOLD', 'color': '#000'} )

    # Sector Trend (Short Term)
    if stock["avg_trend_st"] > 0.5:
        signalsArray.append( {'name': 'Sector Trend (Short Term)', 'signal': 'BUY', 'color': '#009900'} )    
    elif stock["avg_trend_st"] < 0:
        signalsArray.append( {'name': 'Sector Trend (Short Term)', 'signal': 'SELL', 'color': '#ff1a1a'} )    
    else:
        signalsArray.append( {'name': 'Sector Trend (Short Term)', 'signal': 'HOLD', 'color': '#000'} )

    # Institutional Holdings
    if stock['insti'] == 1:
        signalsArray.append( {'name': 'Institutional Holdings', 'signal': 'BUY', 'color': '#009900'} )
    else:
        signalsArray.append( {'name': 'Institutional Holdings', 'signal': '-', 'color': '#000'} )    
    
    # Beat The Insti
    if stock['insti'] == 1 and stock['insti_diff_price'] > 0.1:
        signalsArray.append( {'name': 'Beat The Insti', 'signal': 'BUY', 'color': '#009900'} )
    else:
        signalsArray.append( {'name': 'Beat The Insti', 'signal': '-', 'color': '#000'} )

    # Magic Formula
    if stock['warrant'] == 0 and stock["market_cap"] > 50 and stock['magic_rank'] < 30 and stock['macd_line'] > 0:
        signalsArray.append( {'name': 'Magic Formula', 'signal': 'BUY (Momentum)', 'color': '#009900'} )
    elif stock['warrant'] == 0 and stock["market_cap"] > 50 and stock['magic_rank'] < 30:
        signalsArray.append( {'name': 'Magic Formula', 'signal': 'BUY', 'color': '#009900'} )
    elif stock['magic_rank'] > 700:
        signalsArray.append( {'name': 'Magic Formula', 'signal': 'SELL', 'color': '#ff1a1a'} )
    else:
        signalsArray.append( {'name': 'Magic Formula', 'signal': '-', 'color': '#000'} )

    # Better Than ASB
    if stock['better_than_asb'] > 0:
        signalsArray.append( {'name': 'Better Than ASB', 'signal': 'BUY', 'color': '#009900'} )    
    else:
        signalsArray.append( {'name': 'Better Than ASB', 'signal': '-', 'color': '#000'} )    
    
    # 52-Week High
    if stock['fbo'] > 0:
        signalsArray.append( {'name': '52-Week High', 'signal': 'BUY (Fresh Breakout)', 'color': '#009900'} )
    elif stock['b260'] > -1 and stock['vma5'] > 0:
        signalsArray.append( {'name': '52-Week High', 'signal': 'BUY', 'color': '#009900'} )
    else:
        signalsArray.append( {'name': '52-Week High', 'signal': '-', 'color': '#000'} )    

    # BTST
    if stock['marubozu'] == 1 and stock['higher_vol'] == 1 and stock['higher_spike'] == 1 and stock['no_action'] <= 2 and stock['tava_vol'] == 1:
        signalsArray.append( {'name': 'BTST', 'signal': 'BUY', 'color': '#009900'} )
    else:
        signalsArray.append( {'name': 'BTST', 'signal': '-', 'color': '#000'} )    

    # T+
    if 2 < stock['tplus'] < 8 and stock['tbreak'] == 0:
        signalsArray.append( {'name': 'T+', 'signal': 'BUY', 'color': '#009900'} )
    else:
        signalsArray.append( {'name': 'T+', 'signal': '-', 'color': '#000'} )    

    # Candlestick
    if stock['c_pattern2'] == 1 or stock["bullish_hammer_combo"] > 0:
        signalsArray.append( {'name': 'Candlestick', 'signal': 'BUY', 'color': '#009900'} )
    else:
        signalsArray.append( {'name': 'Candlestick', 'signal': '-', 'color': '#000'} )    

    # Chart Pattern
    if (stock["high_and_tight"] and stock["high_and_tight_upside"] > 1) or (stock["pipe_bottom"] and stock["pipe_upside"] > 1) or (stock["rounding_bot"] and stock["rounding_upside"]):
        signalsArray.append( {'name': 'Chart Pattern', 'signal': 'BUY', 'color': '#009900'} )
    else:
        signalsArray.append( {'name': 'Chart Pattern', 'signal': '-', 'color': '#000'} )    
        
    return signalsArray

# Pivot Point
def pivotPoint(stock):
    pivotArray = []

    # R2 Daily
    if abs(stock['lp1'] - stock['pp_r2']) == stock['closest_pivot']:
        pivotArray.append( {'name': 'R2', 'daily':  stock['pp_r2'], 'colorDaily': '#82CAFA'} )
    else:
        pivotArray.append( {'name': 'R2', 'daily':  stock['pp_r2'], 'colorDaily': '#000'} )
    
    # R1 Daily
    if abs(stock['lp1'] - stock['pp_r1']) == stock['closest_pivot']:
        pivotArray.append( {'name': 'R1', 'daily':  stock['pp_r1'], 'colorDaily': '#82CAFA'} )    
    else:
        pivotArray.append( {'name': 'R1', 'daily':  stock['pp_r1'], 'colorDaily': '#000'} )
    
    # P Daily
    if abs(stock['lp1'] - stock['pp_base']) == stock['closest_pivot']:
        pivotArray.append( {'name': 'P', 'daily':  stock['pp_base'], 'colorDaily': '#82CAFA'} )
    else:
        pivotArray.append( {'name': 'P', 'daily':  stock['pp_base'], 'colorDaily': '#000'} )

    # S1 Daily
    if abs(stock['lp1'] - stock['pp_s1']) == stock['closest_pivot']:
        pivotArray.append( {'name': 'S1', 'daily':  stock['pp_s1'], 'colorDaily': '#82CAFA'} )
    else:
        pivotArray.append( {'name': 'S1', 'daily':  stock['pp_s1'], 'colorDaily': '#000'} )
    
    # S2 Daily
    if abs(stock['lp1'] - stock['pp_s2']) == stock['closest_pivot']:
        pivotArray.append( {'name': 'S2', 'daily':  stock['pp_s2'], 'colorDaily': '#82CAFA'} )        
    else:
        pivotArray.append( {'name': 'S2', 'daily':  stock['pp_s2'], 'colorDaily': '#000'} ) 
    
    # R2 Weekly
    if abs(stock['lp1'] - stock['pp5_r2']) == stock['closest_pivot5']:
        pivotArray[0]['weekly'] = stock['pp5_r2']
        pivotArray[0]['colorWeekly'] = '#82CAFA'
    else:
        pivotArray[0]['weekly'] = stock['pp5_r2']
        pivotArray[0]['colorWeekly'] = '#000'

    # R1 Weekly
    if abs(stock['lp1'] - stock['pp5_r1']) == stock['closest_pivot5']:
        pivotArray[1]['weekly'] = stock['pp5_r1']
        pivotArray[1]['colorWeekly'] = '#82CAFA'
    else:
        pivotArray[1]['weekly'] = stock['pp5_r1']
        pivotArray[1]['colorWeekly'] = '#000'
    
    # P Weekly
    if abs(stock['lp1'] - stock['pp5_base']) == stock['closest_pivot5']:
        pivotArray[2]['weekly'] = stock['pp5_base']
        pivotArray[2]['colorWeekly'] = '#82CAFA'
    else:
        pivotArray[2]['weekly'] = stock['pp5_base']
        pivotArray[2]['colorWeekly'] = '#000'
    
    # S1 Weekly
    if abs(stock['lp1'] - stock['pp5_s1']) == stock['closest_pivot5']:
        pivotArray[3]['weekly'] = stock['pp5_s1']
        pivotArray[3]['colorWeekly'] = '#82CAFA'        
    else:
        pivotArray[3]['weekly'] = stock['pp5_s1']
        pivotArray[3]['colorWeekly'] = '#000'    
    
    # S2 Weekly
    if abs(stock['lp1'] - stock['pp5_s2']) == stock['closest_pivot5']:
        pivotArray[4]['weekly'] = stock['pp5_s2']
        pivotArray[4]['colorWeekly'] = '#82CAFA'        
    else:
        pivotArray[4]['weekly'] = stock['pp5_s2']
        pivotArray[4]['colorWeekly'] = '#000'    

    return pivotArray

stockName = raw_input("Stock Name:")
stock = read_json(stockName)
array = pivotPoint(stock)
# return json.dumps(return_info)
# array = fundamental_ratio_calc(stock)
for row in array:
    print row
