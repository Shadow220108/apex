<h1 align="center">
  <br>
  <img src="https://github.com/Shadow220108/apex/blob/main/assets/apex_banner.png" alt="apex banner">

  <br>
  Apex
  <br>
</h1>
<h3 align="center">
A fully open-sourced compact devboard inspired by the Seed Studio Xiao RP2040 with extra features such as LiPo support 
</h3>

| Front Render | Back Render | 
| --- | --- |
| ![](https://github.com/Shadow220108/apex/blob/main/assets/pcbrenderfront.png) | ![](https://github.com/Shadow220108/apex/blob/main/assets/pcbrenderback.png) | 


| Zine |
| --- |
| ![](https://github.com/Shadow220108/apex/blob/main/assets/apex.png) |

## Features
- **RP2040 MCU** - Dual ARM Cortex-M0+ @ 133MHz MCU.
- **Very compact, XIAO SEEED inspired formfactor**.
- **4 ADC and 7 digital GPIO pins**.
- **5V and 3.3V power pins**.
- Power indicator LED, addressable LED and another RGB LED
- LiPo Battery support and charging circuit
- **USB C** - for programming and power.

## PCB Design 
| ![](https://github.com/Shadow220108/apex/blob/main/assets/pcb(all).jpg) |
|--- |  


 ### The PCB is 4 layers with dimensions 21x17.8mm, made to be easily replacable to any Xiao board.  

 ### All the PCB files are [here](https://github.com/Shadow220108/apex/blob/main/PCB) 

| Front Layer | Inner Layer 1 |
| --- | --- |
| ![](https://github.com/Shadow220108/apex/blob/main/assets/pcb(front).jpg) | ![](https://github.com/Shadow220108/apex/blob/main/assets/pcb(ln1).jpg) |
| Inner Layer 2 | Bottom layer |
| ![](https://github.com/Shadow220108/apex/blob/main/assets/pcb(ln2).jpg) | ![](https://github.com/Shadow220108/apex/blob/main/assets/pcb(back).jpg) |

## Schematics  

Here are the schematic designs,

| ![](https:/github.com/Shadow220108/apex/blob/main/assets/schematics.jpg) |
| --- |

## Why was it made?  

While using the Seed Studio Xiao RP2040 for one of my projects, I realised it doesn't have LiPo support   
and I couldn't use it, unfortunately I had to use a different MCU then, but now I designed one with  
the simplicity of RP2040 with being able to charge LiPo 

## How you can get one for yourself? 

That is pretty easy, you have all the files you will need in the production folder, order the development  
board from any PCB fab ( I chose JLC cause its cheap and has good quality ) and BINGO! You will have it  
to use for any purpose you want!  

## How do you use it?  
You can use it as any normal RP2040 Devboard, enter the boootloader mode  
by holding the BOOT buttom while connecting to your device, flash it with  
firmware and you are good to go!  I have attached a simple code to blink the LED  
available on the board.  

## BOM  
|Name|Purpose          |Quantity|Total Cost (USD)|Link               |Distributor|
|----|-----------------|--------|----------------|-------------------|-----------|
|PCBA|Development Board|2       |79.03           |https://jlcpcb.com/|JLCPCB     |
| | | Total | 79.03 | 

LCSC BOM for the components on board is [here](https://github.com/Shadow220108/apex/blob/main/production/bom.csv)
  


