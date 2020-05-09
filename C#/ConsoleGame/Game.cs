using System;

namespace ConsoleGame
{
  class Game : SuperGame
  {
    public new static void UpdatePosition(string arrow, out int xCor, out int yCor)// changes the position of the character
    {
      switch (arrow)
      {
        case "DownArrow":
          xCor = 0;
          yCor = 1;
          break;
        case "UpArrow":
          xCor = 0;
          yCor = -1;
          break;
        case "LeftArrow":
          xCor = -1;
          yCor = 0;
          break;
        case "RightArrow":
          xCor = 1;
          yCor = 0;
          break;
        
        default:
          xCor = 0;
          yCor = 0;
          break;


      }
    }

    public new static char UpdateCursor(string arrow) //changes the character shown on the screen
    {
      switch(arrow)
      {
        case "DownArrow":
          return 'V';

        case "UpArrow":
          return '^';

        case "LeftArrow":
          return '<';

        case "RightArrow":
          return '>';
        
        default:
          return ' '; 
      }
      
    }

    public new static int KeepInBounds(int xyCor, int maxCor) //without setting the bounds the game would break
    {
      if (xyCor >= maxCor)
      {
        return maxCor-1;
      }
      else if (xyCor < 0)
      {
        return 0;
      }
      else
      {
        return xyCor;
      }

    }

    public new static bool DidScore(int xCor, int yCor, int xFruit, int yFruit) //increases the score if the character hit the object
    {
      if (xCor == xFruit && yCor == yFruit)
      {
        return true;
      }
      else
      {
        return false;
      }

    }
    
  }
}