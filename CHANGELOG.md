# Change Log
All notable changes to this project will be documented in this file.

## [0.0.2] - 2022-02-04

### Added
- Added a contact pattern that combines "Sleeping with spouse or partner" with "Close contact with adult friends and family".
Specifically, contact elements from "Close contact with adult friends and family" were used to fill in blank elements in "Sleeping with spouse or partner".
Added restrictions that use this pattern for members of the public and informed persons supporting the patient:
  - "Sleeping with person and prolonged daytime close contact (>15min)"
  - "Sleeping with informed supporter and prolonged daytime close contact (>15min)"

### Changed
- For contact patterns involving sleeping, sleeping distance changed from 10 cm to 30 cm.
- Removed separate restriction for sleeping with pregnant person or child.
- Changes to restriction names. Now use terms "Prolonged close contact (>15min)" and "informed supporter".


## [0.0.3] - 2022-10-06

### Changed
- Plot method of contact pattern object, in particular the plot of the contact pattern: Changed from plotting the contact distance, d, on the vertical axis to plotting d^(-1.5). A secondary y-axis is shown on the right side of the plot with the corresponding d values.

## [0.0.4] - 2022-10-08

### Changed
- Removed dunder version. Users should instead access the version by:  
    
      importlib.metadata.version("glowgreen")