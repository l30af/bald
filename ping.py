import pygame

# 게임 윈도우 크기
window_width = 600
window_height = 800

# 색 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def main() :
    # Pygame 초기화
    pygame.init()

    # 윈도우 제목
    pygame.display.set_caption("Ping Pong")

    # 윈도우 생성
    screen = pygame.display.set_mode((window_width, window_height))

    # 게임 화면 업데이트 속도
    clock = pygame.time.Clock()

    # 공 초기 위치, 크기, 속도
    ball_x = int(window_width / 2)
    ball_y = int(window_height / 2)
    ball_dx = 4
    ball_dy = 4
    ball_size = 40

    #라켓 크기
    bar_width = 200
    bar_height = 50
    bar_dx = 0
    
    # 라켓 시작 점
    bar_x = bar_start_x = (window_width - bar_width) / 2
    bar_y = bar_start_y = 750

    # 게임 종료 전까지 반복
    done = False

    # 게임 반복 구간
    while not done:
    # 이벤트 반복 구간
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            # 키가 눌릴 경우
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    bar_dx = -5
                elif event.key == pygame.K_RIGHT:
                    bar_dx = 3
            # 키가 놓일 경우
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    bar_dx = 0

        bar_x += bar_dx
        # 게임 로직 구간
        # 속도에 따라 원형 위치 변경
        ball_x += ball_dx

        if ball_x < bar_width: ## bar에 닿았을 때
            if ball_y >= bar_y - ball_size and ball_y <= bar_y + bar_height + ball_size:
                ball_x = bar_width

        # 공이 윈도우를 벗어날 경우
        if (ball_x + ball_size) > window_width or (ball_x - ball_size) < 0:
            ball_dx = ball_dx * -1
        if (ball_y + ball_size) > window_height or (ball_y - ball_size) < 0:
            ball_dy = ball_dy * -1

        # 윈도우 화면 채우기
        screen.fill(WHITE)

        # 화면 그리기 구간
        pygame.draw.circle(screen, BLACK, [ball_x, ball_y], ball_size, 0) # 공 그리기

        pygame.draw.rect(screen, BLACK, (bar_x, bar_y, int(bar_width), int(bar_height))) ## 탁구채

        pygame.display.flip() # 화면 업데이트

        clock.tick(60) # 초당 60 프레임으로 업데이트

    # 게임 종료
    pygame.quit()

if __name__ == "__main__" :
    main()
