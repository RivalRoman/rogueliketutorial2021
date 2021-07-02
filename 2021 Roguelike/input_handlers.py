from typing import Optional

import tcod.event

from actions import Action, EscapeAction, MovementAction


class EventHandler(tcod.event.EventDispatch[Action]):
    def ev_quit(self, event: tcod.event.Quit) -> Optional[Action]:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]:
        action: Optional[Action] = None

        key = event.sym
#movement
        if key == tcod.event.K_UP:
            action = MovementAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = MovementAction(dx=0, dy=1)
        elif key == tcod.event.K_LEFT:
            action = MovementAction(dx=-1, dy=0)
        elif key == tcod.event.K_RIGHT:
            action = MovementAction(dx=1, dy=-1)

#Spells?
        elif key==tcod.event.K_q:
            action = print("you pressed q!")
        elif key==tcod.event.K_w:
            action = print("you pressed w!")
        elif key==tcod.event.K_e:
            action = print("you pressed e!")
        elif key==tcod.event.K_r:
            action = print("you pressed r!")

    


#escape
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction()


        return action
      