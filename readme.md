## Game mechanics
- rotation of blocks is handled by "up arrow" key and is only clockwise
- blocks' velocity is discrete 
- rotations are done using a rotation matrix 
- each shope is rotated around its geometric center 
- in a rotation function, rotate vectors that point to the bottom-left corners instead of the top-left ones because after rotation they will become the coordinates of blocks
- when applying rotation, the origin is set to the center of the block. So we convert between coordinates. 
- each blocks' positions is described using its top-left corner.