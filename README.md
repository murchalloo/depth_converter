# Fork of [Moorchallo's depth_converter](https://github.com/murchalloo/depth_converter)

This app unpacks 32bit .exr depth from 8bbp .bmp screenshot made with [Depth_Tool.fx](https://github.com/BlueSkyDefender/Depth3D/blob/master/Shaders/Others/Depth_Tool.fx) Reshade shader. **It only supports .bmp files**. The export file's being put into _/output_ that creates in the root folder.

### Installation
**step 1**<br/>
1. Download .zip file of the code and unpack it.
2. or
   ```
   git clone https://github.com/sterilija/-fork-depth_converter.git
   ```  
**step 2**<br/>
- Put the ***Depth_Tool.fx*** from _/Shaders_ into your game's _resade-shaders/Shaders_ folder
  
**step 3**<br/>
1. Install TKinter (if it haven't been) [following these instructions](https://tkdocs.com/tutorial/install.html)
2. In the app's root folder run
   ```
   pip install -r requirements.txt
   ```
   to install all the required modules<br/>
  
**step 4**<br/>
- Make screenshot in ReShade ***You should save it as a .bmp file (more instructions are [here](https://framedsc.com/ReshadeGuides/depthguide.htm#high-range-depth-export))***. It should look like this <br/> ![greeny-yellow screenshot of depthmap](https://framedsc.com/Images/depthguide/hrd_goodeg.png)<br/>
  
**step 5**<br/>
- Run the depth_converter.py and enjoy :)

- - - -
# Fork changelog
- Added requirements.txt
- Fixed the *OpenEXR codec is disabled. You can enable it via 'OPENCV_IO_ENABLE_OPENEXR' option* error in depth_converter.py
- Changed the app structure a little bit
- Wrote readable readme.md
