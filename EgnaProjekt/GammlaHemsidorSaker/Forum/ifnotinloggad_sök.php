<?php
echo"
<style>
#searchbar-meny {
  
  margin-top:28.5px;
  margin-right: 200px;
  display: inline-block;
  height: 60px;
  float: right;
  padding: 0;
  position: relative;
}

input[type='text'] {
  height: 30px;
  font-size: 20px;
  display: inline-block;
  font-family: 'myfirstfont';
  border: none;
  outline: none;
  color: #555;
  padding-right: 30px;
  width: 0px;
  position: absolute;
  top: 0;
  right: 0;
  background: none;
  z-index: 3;
  transition: width .5s cubic-bezier(0.000, 0.895, 0.000, 1.000);
  cursor: pointer;

}

input[type='text']:focus:hover {

  border-bottom: 1px solid #BBB;
}

input[type='text']:focus {
  width: 255px;
  z-index: 1;
  border-bottom: 1px solid #BBB;
  cursor: text;
}
</style>
";
?>