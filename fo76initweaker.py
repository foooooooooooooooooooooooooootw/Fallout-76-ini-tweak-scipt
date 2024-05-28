import os
import configparser
from pathlib import Path
import shutil
from stat import S_IREAD, S_IWUSR

home = os.path.expanduser('~')
location = os.path.join(home, 'Documents','My Games', 'Fallout 76')
defaultini = "Fallout76.ini"
baseini = "Fallout76Custom.ini"
prefsini = "Fallout76Prefs.ini"
basefilepath = os.path.join (location, baseini)
prefsfilepath = os.path.join (location, prefsini)
defaultfilepath = os.path.join(location, defaultini)
print(basefilepath)
customexistence = Path(basefilepath)

if customexistence.is_file():
    pass
else:
    shutil.copy(defaultfilepath, os.path.join(location, baseini))
    



print("""
1 - Optimize/Reset ini files
2 - Misc Tweaks
3 - Quit
""")
choice = input("What would you like to do?")
if choice not in ['1', '2', '3']:
    print("input not recognized.")
    choice = input("What would you like to do?")

elif choice == "1":
    print("""
1 - Lowest setting
2 - Author's personal settings
3 - Reset ini
4 - Quit
""")
    choice2 = input(">")
    if choice2 not in ['1', '2', '3', '4']:
        print("input not recognized.")
        choice2 = input(">")
    elif choice2 == "1":
        config = configparser.ConfigParser()
        os.chmod(basefilepath, S_IWUSR|S_IREAD)
        config.read(basefilepath)
        config['Weather']['bPrecipitation'] = "0"
        config['Weather']['bFogEnabled'] = "0"
        config['Weather']['fWindSpeedHighestHighMultiplier'] = "0"
        config['Weather']['bRainOcclusion'] = "0"
        config['Weather']['bWetnessOcclusion'] = "0"
        config['Interface']['fDefaultWorldFOV'] = "70"
        config['Interface']['fDefault1stPersonFOV'] = "80"
        config['Grass']['bAllowCreateGrass'] = "0"

        with open(basefilepath, 'w') as configfile:  
            config.write(configfile)
        os.chmod(basefilepath, S_IREAD)

        config2 = configparser.ConfigParser()
        os.chmod(prefsfilepath, S_IWUSR|S_IREAD)
        config2.read(prefsfilepath)
        config2['Display']['fShadowDistance'] = "0"
        config2['Display']['fDirShadowDistance'] = "0"
        config2['Display']['iShadowMapResolution'] = "1024"
        config2['Display']['bVolumetricLightingEnable'] = "0"
        config2['Display']['iDirShadowSplits'] = "1"
        config2['Display']['fBlendSplitDirShadow'] = "0"
        config2['Display']['bSAOEnable'] = "0"
        config2['ImageSpace']['bScreenSpaceBokeh'] = "0"
        config2['ImageSpace']['bDoDepthOfField'] = "0"
        config2['ImageSpace']['bLensFlare'] = "0"
        config2['LightingShader']['bScreenSpaceReflections'] = "0"
        config2['Water']['bUseWaterHiRes'] = "0"
        config2['Water']['bUseWaterDisplacements'] = "0"
        config2['Water']['bUseWaterRefractions'] = "0"
        config2['Water']['bUseWaterReflections'] = "0"
        config2['Water']['bUseWaterDepth'] = "0"
        with open(prefsfilepath, 'w') as configfile2:  
            config2.write(configfile2)
        os.chmod(prefsfilepath, S_IREAD)

    elif choice2 == "2":
        config = configparser.ConfigParser()
        os.chmod(basefilepath, S_IWUSR|S_IREAD)
        config.read(basefilepath)
        config['General']['bPlayMainMenuMusic'] = "0"
        config['General']['sIntroSequence'] = ""
        config['Weather']['bPrecipitation'] = "0"
        config['Weather']['bFogEnabled'] = "0"
        config['Weather']['fWindSpeedHighestHighMultiplier'] = "0"
        config['Weather']['bRainOcclusion'] = "0"
        config['Weather']['bWetnessOcclusion'] = "1"
        config['Interface']['fDefaultWorldFOV'] = "110"
        config['Interface']['fDefault1stPersonFOV'] = "110"
        config['Grass']['bAllowCreateGrass'] = "0"

        with open(basefilepath, 'w') as configfile:  
            config.write(configfile)
        os.chmod(basefilepath, S_IREAD)

        config2 = configparser.ConfigParser()
        os.chmod(prefsfilepath, S_IWUSR|S_IREAD)
        config2.read(prefsfilepath)
        config2['Display']['fShadowDistance'] = "2500"
        config2['Display']['fDirShadowDistance'] = "2500"
        config2['Display']['iShadowMapResolution'] = "1024"
        config2['Display']['bVolumetricLightingEnable'] = "1"
        config2['Display']['iDirShadowSplits'] = "1"
        config2['Display']['iPresentInterval'] = "0"
        config2['Display']['fBlendSplitDirShadow'] = "0"
        config2['Display']['bSAOEnable'] = "1"
        config2['ImageSpace']['bScreenSpaceBokeh'] = "0"
        config2['ImageSpace']['bDoDepthOfField'] = "0"
        config2['ImageSpace']['bLensFlare'] = "0"
        config2['LightingShader']['bScreenSpaceReflections'] = "0"
        config2['Water']['bUseWaterHiRes'] = "1"
        config2['Water']['bUseWaterDisplacements'] = "0"
        config2['Water']['bUseWaterRefractions'] = "0"
        config2['Water']['bUseWaterReflections'] = "0"
        config2['Water']['bUseWaterDepth'] = "1"
        with open(prefsfilepath, 'w') as configfile2:  
            config2.write(configfile2)
        os.chmod(prefsfilepath, S_IREAD)
        quit

    elif choice2 == "3":
        ##Defaults for base ini file
        config = configparser.ConfigParser()
        os.chmod(basefilepath, S_IWUSR|S_IREAD)
        config.read(basefilepath)

        config['General']['bPlayMainMenuMusic'] = "1"
        config['General']['sIntroSequence'] = "BGSLogo4k.bk2"
        config['Weather']['bPrecipitation'] = "1"
        config['Weather']['bFogEnabled'] = "1"
        config['Weather']['fWindSpeedHighestHighMultiplier'] = "1.5"
        config['Weather']['bRainOcclusion'] = "1"
        config['Weather']['bWetnessOcclusion'] = "1"
        config['Interface']['fDefaultWorldFOV'] = "70"
        config['Interface']['fDefault1stPersonFOV'] = "80"
        config['Grass']['bAllowCreateGrass'] = "1"
        with open(basefilepath, 'w') as configfile:  
            config.write(configfile)
        os.chmod(basefilepath, S_IREAD)

        ## Defaults for prefs ini file
        config2 = configparser.ConfigParser()
        os.chmod(prefsfilepath, S_IWUSR|S_IREAD)
        config2.read(prefsfilepath)
        config2['Display']['fShadowDistance'] = "10000"
        config2['Display']['fDirShadowDistance'] = "10000"
        config2['Display']['iShadowMapResolution'] = "1024"
        config2['Display']['bVolumetricLightingEnable'] = "1"
        config2['Display']['iDirShadowSplits'] = "3"
        config2['Display']['iPresentInterval'] = "1"
        config2['Display']['fBlendSplitDirShadow'] = "0"
        config2['Display']['bSAOEnable'] = "1"
        config2['ImageSpace']['bScreenSpaceBokeh'] = "1"
        config2['ImageSpace']['bDoDepthOfField'] = "1"
        config2['ImageSpace']['bLensFlare'] = "1"
        config2['LightingShader']['bScreenSpaceReflections'] = "1"
        config2['Water']['bUseWaterHiRes'] = "1"
        config2['Water']['bUseWaterDisplacements'] = "1"
        config2['Water']['bUseWaterRefractions'] = "1"
        config2['Water']['bUseWaterReflections'] = "1"
        config2['Water']['bUseWaterDepth'] = "1"
        with open(prefsfilepath, 'w') as configfile2:  
            config2.write(configfile2)
        os.chmod(prefsfilepath, S_IREAD)
        quit
    
    elif choice2 == "4":
        quit
    
elif choice == "2":
    print("""
1 - Uncap Framerate
2 - Disable Startup Video
3 - Disable Main Menu Music
4 - Change FOV
5 - Quit
""")
    choice3 = input(">")
    if choice3 not in ['1', '2', '3', '4', '5']:
        print("input not recognized.")
        choice3 = input(">")
    elif choice3 == "1":
        config2 = configparser.ConfigParser()
        os.chmod(prefsfilepath, S_IWUSR|S_IREAD)
        config2.read(prefsfilepath)
        config2['Display']['iPresentInterval'] = "0"
        with open(prefsfilepath, 'w') as configfile2:  
            config2.write(configfile2)
        os.chmod(prefsfilepath, S_IREAD)
        print("Ensure to cap your game framerate at 120. Going over 120 might cause many undesirable effects.")
        choice3 = input(">")
        if choice3 not in ['1', '2', '3', '4', '5']:
            print("input not recognized.")
            choice3 = input(">")
    elif choice3 == "2":
        config = configparser.ConfigParser()
        os.chmod(basefilepath, S_IWUSR|S_IREAD)
        config.read(basefilepath)
        config['General']['sIntroSequence'] = ""
        with open(basefilepath, 'w') as configfile:  
            config.write(configfile)
        os.chmod(basefilepath, S_IREAD)
        choice3 = input(">")
        if choice3 not in ['1', '2', '3', '4', '5']:
            print("input not recognized.")
            choice3 = input(">")
    elif choice3 == "3":
        config = configparser.ConfigParser()
        os.chmod(basefilepath, S_IWUSR|S_IREAD)
        config.read(basefilepath)
        config['General']['bPlayMainMenuMusic'] = "0"
        config['General']['uMainMenuMusicAttnmB'] = "9999999"
        with open(basefilepath, 'w') as configfile:
            config.write(configfile)
        os.chmod(basefilepath, S_IREAD)
        choice3 = input(">")
        if choice3 not in ['1', '2', '3', '4', '5']:
            print("input not recognized.")
            choice3 = input(">")
    elif choice3 == "4":
        config = configparser.ConfigParser()
        os.chmod(basefilepath, S_IWUSR|S_IREAD)
        config.read(basefilepath)
        fov = input("What FOV would you like? (70-120)")
        if fov.isdigit and fov <= 120 and fov >= 70:
            config['Interface']['fDefaultWorldFOV'] = fov
            config['Interface']['fDefault1stPersonFOV'] = fov
            with open(basefilepath, 'w') as configfile:  
                config.write(configfile)
            os.chmod(basefilepath, S_IREAD)
        else:
            print("input not recognized or wrong")
            quit
    elif choice3 == "5":
        quit
elif choice == "3":        
    quit


