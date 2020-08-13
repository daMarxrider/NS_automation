import logging
from JoycontrolPlugin import JoycontrolPlugin

logger = logging.getLogger(__name__)

class SamplePlugin(JoycontrolPlugin):
    async def run(self):
        logger.info('This is sample joycontrol plugin!')
        await self.wait(20)
        await self.button_push('home')
        await self.wait(5)
        await self.button_push('home')
        for i in range(0,20):
            logger.info(f'Plugin Options: {self.options}')
            await self.button_push('home')
            await self.wait(1)
            
            await self.button_push('a')
            await self.wait(1)
            await self.button_push('a')
            await self.wait(5)
            await self.button_push('home')
            await self.wait(5)
            await self.button_push('down')
            await self.wait(1)
            await self.button_push('right')
            await self.wait(1)
            await self.button_push('right')
            await self.wait(1)
            await self.button_push('right')
            await self.wait(1)
            await self.button_push('right')
            await self.wait(1)
            await self.button_push('a')
            await self.wait(2)
            for i in range(0,14):
                await self.button_push('down')
                await self.wait(1)
            await self.button_push('a')
            await self.wait(1)
            for i in range(0,4):
                await self.button_push('down')
                await self.wait(1)
            await self.button_push('a')
            await self.wait(1)
            for i in range(0,2):
                await self.button_push('down')
                await self.wait(1)
            await self.button_push('a')
            await self.wait(1)
            await self.button_push('up')
            await self.wait(1)
            for i in range(0,5):
                await self.button_push('right')
                await self.wait(1)
            await self.button_push('a')
            await self.wait(1)
            for i in range(0,2):
                await self.button_push('home')
                await self.wait(1)


        logger.info('Tilt the left stick down')
        await self.left_stick('down')
        await self.wait(10.3)
